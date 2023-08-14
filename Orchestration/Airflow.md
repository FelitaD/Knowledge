
Orchestration framework

# What is Airflow

Airflow est un outil open source qui d'automatisation et d'orchestration développé en Python par les équipes de AirBNB dans les années 2010.
Airflow propose de nombreuses fonctionnalités pour mettre en place des pipelines d'actions, pour les automatiser, pour les surveiller... De plus, Airflow permet de gérer un ensemble d'utilisateurs en leur attribuant différents rôles. Enfin, à l'heure où les entreprises se tournent de plus en plus vers le Cloud, Airflow permet une intégration simple de ces technologies.

![Untitled](Attachments/Airflow%2056665e55352845c49ff0219270620ff0/Untitled.png)

- Airflow is an orchestrator, not a processing framework, process your gigabytes of data outside of Airflow (i.e. You have a Spark cluster, you use an operator to execute a Spark job, the data is processed in Spark).

# How Airflow works

## One Node Architecture
	
Executor updates status of the tasks in the metastore

Queue defines the order of tasks (part of the executor when single node)

![Untitled](Attachments/Airflow%2056665e55352845c49ff0219270620ff0/Untitled%201.png)

## Multi Nodes Architecture (Celery) → production (k8s)

![Untitled](Attachments/Airflow%2056665e55352845c49ff0219270620ff0/Untitled%202.png)

## How tasks are scheduled / executed
	
Dag Run = instance of the dag

![Untitled](Attachments/Airflow%2056665e55352845c49ff0219270620ff0/Untitled%203.png)

![Untitled](Attachments/Airflow%2056665e55352845c49ff0219270620ff0/Untitled%204.png)

![Untitled](Attachments/Airflow%2056665e55352845c49ff0219270620ff0/Untitled%205.png)

![Untitled](Attachments/Airflow%2056665e55352845c49ff0219270620ff0/Untitled%206.png)

![Untitled](Attachments/Airflow%2056665e55352845c49ff0219270620ff0/Untitled%207.png)
	
# Core components
- A `DAG` is a data pipeline, an `Operator` is a task.
- An `Executor` defines how your tasks are execute whereas a `worker` is a process executing your task
- The `scheduler` schedules your tasks, the `web server` serves the UI, the `database` stores the metadata of Airflow.

# CLI

`airflow db init` : the first command to execute to initialise Airflow

`airflow db upgrade`

`airflow db reset`

`airflow webserver`

`airflow scheduler`

`airflow dags list` → file path of the dag

`airflow tasks list {DAG_ID}` → list tasks of data pipeline

`airflow dags trigger -e 2020-01-01 {DAG_ID}` → execute + date + dag

# UI

Gantt : sequential no overlap

![Untitled](Attachments/Airflow%2056665e55352845c49ff0219270620ff0/Untitled%208.png)

- The Gantt view is super useful to spot bottlenecks and tasks that are too long to execute

# DAGs

## Intro

Airflow est un outil qui permet d'organiser un ensemble de tâches en leur donnant des dépendances, c'est-à-dire des conditions sur l'exécution de ces tâches. Pour définir ces dépendances, on utilise un `DAG`
, diminutif de `Directed Acyclic Graph`
(arêtes ne vont que dans un sens + on ne peut pas passer deux fois au même endroit)

![Untitled](Attachments/Airflow%2056665e55352845c49ff0219270620ff0/Untitled%2010.png)

- `Task` représente une unité de travail théorique: on peut oser la comparaison avec une fonction Python, qui tant qu'elle n'est pas appelée ne représente que un ensemble d'actions potentielles.
	- `Operator` sont des objets qui permettent d'utiliser des outils différents. Airflow propose un ensemble d'`Operator` prédéfini parmi lesquels on retrouve les `BashOperator` ou les `PythonOperator` qui permettent l'exécution d'une tâche Bash ou Python respectivement. On trouve beaucoup d'autres `Operator` qui permettent d'utiliser d'autres outils comme des bases de données (`MySqlOperator`, `PostgresOperator`, ...), des outils comme `Docker` (`DockerOperator`), ou des outils de communication (`EmailOperator`, `SlackOperator`, ...), ...
    
Pour l'instant, nous n'avons abordé que la définition du travail à effectuer. Lorsque l'on définit un `DAG`, on peut définir la fréquence à laquelle celui-ci s'exécute. On peut choisir d'avoir un DAG qui est exécuté de manière récurrente ou simplement une fois.

Lorsqu'on déclenche (en anglais `trigger`) un DAG, il s'exécute une première fois. On parle alors d'un `DAG run`. Si on a défini une fréquence de répétition pour le DAG, alors il se ré-exécutera à un intervalle de temps donné. Lorsqu'un `DAG` est lancé, chacune des `Task` de ce `DAG` est lancée en suivant l'ordre défini par le `DAG`. Pour chaque tâche lancée, on crée une instance de cette tâche, en anglais une `Task instance`.

## Operators
- `BashOperator` : exécute une commande bash,
- `PythonOperator` : exécute une fonction Python,
- `EmailOperator` : envoie un mail,
- `DockerOperator` : exécute une commande dans un container Docker,
- `HttpOperator` : effectue une requête sur un endpoint HTTP,
- etc…

[airflow.operators - Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/index.html)

vous pouvez bien sûr créer les vôtres si besoin

Pour l’aspect technique, un operator est tout simplement une classe Python héritant de `BaseOperator`. Lorsque la tâche est appelée, la fonction `execute()` de l’operator est exécutée. Vous l’aurez compris, un operator instancié devient donc une tâche.

## Simple Task

Les exigences minimales pour définir une `Task` avec le `PythonOperator` sont de lui fournir un `task_id` qui servira d'identifiant à la `Task` et un `python_callable`, c'est-à-dire une fonction Python qui sera exécutée. On passe aussi le `dag` auquel cette tâche appartient.

```python
from airflow.operators.python import PythonOperator
import datetime

# definition of the function to execute
def print_date_and_hello():
	print(datetime.datetime.now())
	print('Hello from Airflow')

my_task = PythonOperator(
	task_id='my_very_first_task',
	python_callable=print_date_and_hello,
	dag=my_dag
)
```

## Enregistement

Si on veut qu'Airflow prenne en compte ce DAG, il nous faut l'enregistrer dans Airflow, c'est-à-dire coller le fichier dans le dossiers `dags` et attendre que Airflow ait pris en compte ce nouveau `DAG`.

## Plusieurs tâches

```python
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

my_dag = DAG(
	dag_id='my_second_dag',
	description='A new DAG with two tasks',
	tags=['tutorial', 'datascientest'],
	schedule_interval=None,
	default_args={
		'owner': 'airflow',
		'start_date': days_ago(2),
	}
)

def print_task1():
	print('hello from task 1')

def print_task2():
	print('hello from task 2')

task1 = PythonOperator(
	task_id='second_dag_task1',
	python_callable=print_task1,
	dag=my_dag
)

task2 = PythonOperator(
	task_id='second_dag_task2',
	python_callable=print_task2,
	dag=my_dag
)
```

## Dépendances

Ajouter dans le DAG `task1 >> task2`

```python
pantalon >> [chaussette_d, chaussette_g]

chaussette_d >> chaussure_d
chaussette_g >> chaussure_g

[chaussure_g, chaussure_d] >> sortir
```

![Untitled](Attachments/Airflow%2056665e55352845c49ff0219270620ff0/Untitled%2011.png)

## Passer des arguments

```python
def print_text(clothes):
	print('hello from task 1')

pantalon = PythonOperator(
	task_id='pantalon',
	python_callable=print_text,
	dag=my_dag,
	op_kwargs={'clothes': 'pantalon'}
)
```

## Récurrence
- Rappel cronjob

`23 0-20/2 * * 1,6-7`

- à la 23ème minute
- toutes les deux heures 
 entre minuit et 20h
- les lundis, samedis et dimanches.

[Crontab.guru - The cron schedule expression editor](https://crontab.guru/)


```python
'start_date': days_ago(0, minute=1),
	},
	catchup=False
```

## Conditions

### `trigger_rule`
- `all_success`: (valeur par défaut) toutes les tâches parentes doivent avoir réussi
- `all_done`: toutes les tâches parentes ont été exécutées (peu importe le statut)
- `one_success`: au moins une tâche parente a réussi
- `one_failed`: au moins une tâche parente a échoué
- `none_failed`: toutes les tâches parentes ont réussi ou ont été passées.
- ...
- code

```python
import random
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

my_dag = DAG(
	dag_id='fork1_dag',
	tags=['tutorial', 'datascientest'],
	schedule_interval=None,
	default_args={
		'owner': 'airflow',
		'start_date': days_ago(0, minute=1)
	},
	catchup=False
)

def successful_task():
	print('success')

def failed_task():
	raise Exception('This task did not work!')

def random_fail_task():
	random.seed()
	if random.random() < .9:
		raise Exception('This task randomly failed')

task1 = PythonOperator(
	task_id='task1',
	python_callable=successful_task,
	dag=my_dag
)

task2 = PythonOperator(
	task_id='task2',
	python_callable=failed_task,
	dag=my_dag
)

task3 = PythonOperator(
	task_id='task3',
	python_callable=successful_task,
	dag=my_dag,
	trigger_rule='all_done'
)

[task1, task2] >> task3
```
	
### `retries` et `retry_delay`

Relancer un tache si elle a échoué en précisant temps d’attente

```python
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
import datetime

my_dag = DAG(
	dag_id='retries_dag',
	description='My DAG that will try but fail',
	tags=['tutorial', 'datascientest'],
	schedule_interval=None,
	default_args={
		'owner': 'airflow',
		'start_date': days_ago(0, minute=1),
	},
	catchup=False
)

def failed_task():
	raise Exception('This task did not work!')

task1 = PythonOperator(
	task_id="my_failed_task",
	python_callable=failed_task,
	retries=5,
	retry_delay=datetime.timedelta(seconds=30),
	dag=my_dag
)
```

### emails en cas d’échec

- `email` avec une liste d'adresses e-mail destinataires
- `email_on_retry` (ou `email_on_failure` avec un booléen)

```bash
AIRFLOW__SMTP__SMTP_HOST=smtp.gmail.com
AIRFLOW__SMTP__SMTP_PORT=587
AIRFLOW__SMTP__SMTP_USER=de.airflow@gmail.com
AIRFLOW__SMTP__SMTP_PASSWORD=Airflow123
AIRFLOW__SMTP__SMTP_MAIL_FROM=de.airflow@gmail.com
```

```python

task1 = PythonOperator(
	task_id="my_failed_task",
	python_callable=failed_task,
	retries=5,
	retry_delay=datetime.timedelta(seconds=30),
	dag=my_dag,
	email_on_retry=True,
	email=['john.doe@datascientest.com']
)
```

## Subdags

Lancer un dag depuis un autre dag grâce à l’opérateur `SubDagOperator`

- Fonction retournant un subdag

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

def create_sub_dag(dag_id, schedule_interval, start_date):
	my_sub_dag = DAG(
		dag_id=dag_id,
		schedule_interval=schedule_interval,

		default_args={
			'start_date': days_ago(0)
		}
	)

	task1 = BashOperator(
		bash_command="echo subdag task 1",
		task_id="my_sub_dag_task1",
		dag=my_sub_dag
	)

	task2 = BashOperator(
		bash_command="echo subdag task 2",
		task_id="my_sub_dag_task2",
		dag=my_sub_dag
	)

	task1 >> task2

	return my_sub_dag
```

- DAG parent

```python
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.subdag import SubDagOperator
from airflow.operators.bash import BashOperator
# importing DAG generating function
from sub_dag import create_sub_dag

my_parent_dag = DAG(
	dag_id="parent_to_subdag",
	schedule_interval=None,
	default_args={
		'owner': 'airflow',
		'start_date': days_ago(0, 1)
	}
)

task1 = SubDagOperator(
	task_id="my_subdag",
	subdag=create_sub_dag(
		dag_id=my_parent_dag.dag_id + '.' + 'my_subdag',
		schedule_interval=my_parent_dag.schedule_interval,
		start_date=my_parent_dag.start_date),
	dag=my_parent_dag
)

task2 = BashOperator(
	task_id="bash_task",
	bash_command="echo hello world from parent",
	dag=my_parent_dag
)

task1 >> task2
```


Subdag accessible en cliquant “Zoom into subdag”

## XComs

Transmettre des données d’une tâche à une autre

Valeur dans Admins > XComs

- Ajouter `return`

```python
def function_with_return():
	return random.uniform(a=0, b=1)
```

- Nommer les XComs `task_instance.xcom_push`

```python
def function_with_return(task_instance):
	task_instance.xcom_push(
		key="my_xcom_value",
		value=random.uniform(a=0, b=1)
	
```

- `task_instance.xcom_pull`

```python
def read_return(task_instance):
	print(task_instance.xcom_pull(
			key="my_xcom_value",
			task_ids=['python_task']))

my_read_task = PythonOperator(
	task_id='my_read_task',
	dag=my_dag,
	python_callable=read_return
)

my_task >> my_read_task
```

- XCom sous forme de dict

```python
def function_with_return(task_instance):
	task_instance.xcom_push(
		key="my_xcom_value",
		value={
			"hello": "world",
			"bonjour": "le monde"
		}
	)
```

- Stockage
- XComs sont stockées dans la base de données interne d'Airflow
- les valeurs d'un `XCom`
 doivent être limitées à 48KB
- ces valeurs doivent être sérialisables: on ne peut pas mettre n'importe quel objet dans un `XCom`
- définies et accessibles à l'intérieur d'un même `DAG`
- `Variable` XCom accessible par tous les DAG

`Variable.set(key="key", value="value")`

```python
from airflow.models import Variable
my_variable_value = Variable.get(key="my_variable")
```

## Sensors et Connections
- présence d’un fichier
- disponibilité d’une BDD
- ...
- `Connection`

contient les infos relatives à un système de stockage ...

Admin > Connection

- `Conn Id`: identifiant de la `Connection` prend la valeur `my_filesystem_connection`
- `Conn Type`: type de `Connection` prend la valeur `File (path)`
- `Login` prend la valeur `airflow`
- `Password` prend la valeur `airflow`
- `Extra` doit contenir la valeur `{"path": "/tmp/"}`
- `FileSensor`

vérifier qu’un fichier existe

- `dag_sensor.py`
- `poke_interval` : intervalle entre 2 tentatives de trouver le fichier
- `fs_conn_id` : connection à utiliser
- `timeout` : temps au bout duquel échec
- `mode='reschedule'` : ne pas prolonger l’exécution de la tache entre 2 tentatives

```python
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator

my_dag = DAG(
	dag_id='sensor_dag',
	schedule_interval=None,
	start_date=days_ago(0)
)

my_sensor = FileSensor(
	task_id="check_file",
	fs_conn_id="my_filesystem_connection",
	filepath="my_file.txt",
	poke_interval=30,
	dag=my_dag,
	timeout=5 * 30,
	mode='reschedule'
)

my_task = BashOperator(
	task_id="print_file_content",
	bash_command="cat /tmp/my_file.txt",
	dag=my_dag
)

my_task >> my_sensor
```

# Gestion des utilisateurs

Role Based Access Control

Security > List Users

# Documentation

Une fois que ce `DAG` est enregistré, on peut voir la documentation sur 

- le `DAG` directement dans le menu du `DAG` (`DAG Docs`).
- la documentation des tâches: `Graph View` et en cliquant sur une tâche puis sur `Instance Details`

Avec `doc_md`, la documentation est traitée comme du `markdown` et est donc mise en forme.

```python
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
import time

my_dag = DAG(
    dag_id="documented_dag",
    doc_md="""# Documented DAG
This `DAG` is documented and the next line is a quote:

> Airflow is nice

This DAG has been made:

* by Paul
* with documentation
* with caution
    """,
    start_date=days_ago(0),
    schedule_interval=None
)

def sleep_1_sec():
    time.sleep(1)

task1 = PythonOperator(
    task_id="sleep1",
    python_callable=sleep_1_sec,
    doc_md="""# Task1

Task that is used to sleep for 1 sec""",
    dag=my_dag
)

task2 = PythonOperator(
    task_id="sleep2",
    python_callable=sleep_1_sec,
    doc="""Task 3

It has an ugly description.
    """,
    dag=my_dag
)
```

### ****Environnement d'exécution et Pools****

`Executor` : permet de changer l'environnement d'exécution (avec K8s, autres gestionnaires...)

`Pools` : limiter l’execution de taches concurrentes (sequentiel / parallele)

- nombre de `Slots` : nombre de taches qui s’executent parallelement
- `Pool` par défaut contient 128 slots

Admin > Pools

micro_pool : 1 Slot

DAG prenant avec 3 taches de 1 minutes → 3 minutes car 1 seul Slot

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import time

def wait_1_minute():
    time.sleep(60)

my_dag = DAG(
    dag_id="concurrent_dag",
    schedule_interval=None,
    start_date=days_ago(0),
    default_args={
        **'pool': 'micro_pool'**
    }
)

task1 = PythonOperator(
    task_id="wait1",
    python_callable=wait_1_minute,
    dag=my_dag
)

task2 = PythonOperator(
    task_id="wait2",
    python_callable=wait_1_minute,
    dag=my_dag
)

task3 = PythonOperator(
    task_id="wait3",
    python_callable=wait_1_minute,
    dag=my_dag
)
```

# Plugins

Les `Plugins` Airflow sont des processus qui permettent de relier Airflow à d'autres outils. 

Par exemple, si l'organisation a l'habitude de surveiller des processus en utilisant `Prometheus`, on peut utiliser un Plugin qui renverra des informations sur le statut du cluster Airflow et le statut des tâches en cours. 

On peut aussi facilement relier Airflow à certaines bases de données

[Airflow Plugins](https://github.com/airflow-plugins/)

# Clients

CLI [https://airflow.apache.org/docs/apache-airflow/stable/usage-cli.html](https://airflow.apache.org/docs/apache-airflow/stable/usage-cli.html)

Doc API [https://airflow.apache.org/docs/apache-airflow/2.2.4/](https://airflow.apache.org/docs/apache-airflow/2.2.4/)

# Best practices

[Best Practices - Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/2.1.4/best-practices.html)

- réduire au maximum la taille des tâches pour qu'elles puissent tourner ou re-tourner de manière indépendantes
- éviter de faire tourner du code en dehors de la définition des tâches et des `DAGs` dans le dossier `dags`
- éviter d'utiliser Airflow pour des tâches sur de trop gros volumes de données: préférer lancer des tâches sur des moteurs de calcul dédiés (Spark, Hadoop, SQL, ...)
- contrairement à ce que nous avons fait dans le cours, préférer un `start_date` statique
- passer la plupart des arguments communs aux différentes tâches dans l'argument `default_args` dans la définition du `DAG`
- éviter de supprimer des tâches dans un `DAG` pour conserver l'historique d'exécution de ces tâches: préférer construire un nouveau `DAG`
- implémenter des tâches de vérifications avec des `Sensors` notamment après des insertions
- bien documenter les tâches et les `DAG`

## Best practices with new tasks : `test`

`airflow tasks test ...`
*command layout :* `command subcommand dag_id task_id date`

# Resources

[ETL Pipelines with Airflow: the Good, the Bad and the Ugly | Airbyte](https://www.notion.so/ETL-Pipelines-with-Airflow-the-Good-the-Bad-and-the-Ugly-Airbyte-a93ca6b5fcc04001ba7d68dde3957c88)

[Concepts — Airflow Documentation](https://www.notion.so/Concepts-Airflow-Documentation-5ce5c7a9799143b3a109093862a70937)

[Scheduler Performance— Airflow Documentation](https://www.notion.so/Scheduler-Performance-Airflow-Documentation-67c542dc37cc430995ee4c0c39957739)

[python - How to control the parallelism or concurrency of an Airflow installation? - Stack Overflow](https://www.notion.so/python-How-to-control-the-parallelism-or-concurrency-of-an-Airflow-installation-Stack-Overflow-7f9a5e4c1fc04529a34f8586b248f02d)

[Customising Airflow: Beyond Boilerplate Settings](https://www.notion.so/Customising-Airflow-Beyond-Boilerplate-Settings-d54e68558de14321ba098887a97004f5)