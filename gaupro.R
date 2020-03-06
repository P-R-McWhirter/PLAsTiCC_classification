gaupro <- function(){
  
  library(kernlab)
  
  # train model
  data(iris)
  test <- gausspr(Species~.,data=iris,var=2)
  test
  alpha(test)
  
  # predict on the training set
  predict(test,iris[,-5])
  # class probabilities 
  predict(test, iris[,-5], type="probabilities")
  
  # create regression data
  x <- training_set[which(training_set$object_id == training_set_metadata$object_id[which(training_set_metadata$target == levels(as.factor(training_set_metadata$target))[12])][i] & training_set$passband == 2),2]
  y <- training_set[which(training_set$object_id == training_set_metadata$object_id[which(training_set_metadata$target == levels(as.factor(training_set_metadata$target))[12])][i] & training_set$passband == 2),4]
  
  # regression with gaussian processes
  foo <- gausspr(x, y, scaled = TRUE, type= NULL, kernel="polydot",
                 kpar="automatic", var=1, variance.model = FALSE, tol=0.0005,
                 cross=0, fit=TRUE, subset, na.action = na.omit)
  foo
  
  # predict and plot
  ytest <- predict(foo, x)
  plot(x, y, type ="p")
  lines(x, ytest, col="red")
  
}