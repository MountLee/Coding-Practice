library(doParallel)
library(foreach)


my_f <- function(i){
  # Sys.sleep(2)
  
  message <- glue::glue("this is the {i}-th task") # paste( )
  return(message)
}

num_cores <- detectCores()

# if each single task is too simple, then parallelization may not show outperformance
{
  n_work <- 12000
  print("--------------- parallel ----------------")
  
  t1 <- Sys.time()
  cl <- makeCluster(num_cores)
  registerDoParallel(cl)
  
  t2 <- Sys.time()
  test <- foreach(x = 1:n_work, .combine = 'c') %dopar% my_f(x)
  stopCluster(cl)
  
  t3 <- Sys.time()
  print(t3 - t1)
  print(t3 - t2)
  
  print("--------------- lapply ----------------")
  t1 <- Sys.time()
  test <- lapply(c(1:n_work), FUN = my_f)
  t2 <- Sys.time()
  print(t2 - t1)
  # test
  
  
  print("--------------- for loop ----------------")
  t1 <- Sys.time()
  test <- vector(mode = 'character', length = n_work)
  for (i in 1:n_work){
    test[i] <- my_f(i)
  }
  t2 <- Sys.time()
  print(t2 - t1)
}
  
  

# now make each single task more complex
# it can be seen that parallelization completes the task in much shorter time
my_f <- function(i, rep = 10000){
  # Sys.sleep(2)
  sub_task <- c()
  for (ii in 1:rep){
    k <- "SOMETHING"
    sub_task <- c(sub_task,tolower(k))
  }
  message <- glue::glue("this is the {i}-th task") # paste( )
  return(message)
}

num_cores <- detectCores()

{
  n_work <- 120
  print("--------------- parallel ----------------")
  
  t1 <- Sys.time()
  cl <- makeCluster(num_cores)
  registerDoParallel(cl)
  
  t2 <- Sys.time()
  test <- foreach(x = 1:n_work, .combine = 'c') %dopar% my_f(x)
  stopCluster(cl)
  
  t3 <- Sys.time()
  print(t3 - t1)
  print(t3 - t2)
  
  print("--------------- lapply ----------------")
  t1 <- Sys.time()
  test <- lapply(c(1:n_work), FUN = my_f)
  t2 <- Sys.time()
  print(t2 - t1)
  
  print("--------------- for loop ----------------")
  t1 <- Sys.time()
  test <- vector(mode = 'character', length = n_work)
  for (i in 1:n_work){
    test[i] <- my_f(i)
  }
  t2 <- Sys.time()
  print(t2 - t1)
}





x <- c(1:100)/100
y <- tanh(x)
plot(x,y)

