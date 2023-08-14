f <- function(num = 1){
        hello <- "Hello World!\n"
        for(i in seq_along(num)) {
                cat(hello)
        }
        chars <- nchar(hello) * num
        chars
}
meaningoflife <- f(3)
meaningoflife(3)

paste
args(paste)
