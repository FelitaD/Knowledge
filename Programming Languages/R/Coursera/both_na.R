x <- c(1, 2, NA, 3, NA)
y <- c(NA, 3, NA, 3, 4)
x_na <- is.na(x)
y_na <- is.na(y)
xy_na <- x_na & y_na
both_na <- sum(xy_na)
z <- c(a = list(3,4,5), b = list(8, 9, 10))

last_row <- function(df) {
        df[nrow(df),  , drop = TRUE]
        }


df <- data.frame(
        a = 1L,
        b = 1.5,
        y = Sys.time(),
        z = ordered(1)
)

A <- sapply(df[1:4], class) 
B <- sapply(df[3:4], class)

