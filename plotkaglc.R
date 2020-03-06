plotkaglc <- function(objid, type = "t"){
  
  int_t <- read.csv(paste("F:/Documents/Kaggle/Results/int_", objid, "_", type, ".csv", sep=""), header=FALSE)
  
  print(training_set_metadata[which(training_set_metadata$object_id == objid),])
  
  minval <- floor(min(int_t))
  
  maxval <- ceiling(max(int_t))
  
  if (type == "t"){
  
    plot(seq(0, 1200, length.out = 10000), int_t[1,], type = "l", col = "purple", xlim = c(0, 1200), ylim = c(minval, maxval), main = paste("Object ", objid, " Interpolated Light Curve", sep=""), xlab = "Time (days)", ylab = "Flux")
  
    lines(seq(0, 1200, length.out = 10000), int_t[2,], col = "blue")
    
    lines(seq(0, 1200, length.out = 10000), int_t[3,], col = "green")
    
    lines(seq(0, 1200, length.out = 10000), int_t[4,], col = "orange")
    
    lines(seq(0, 1200, length.out = 10000), int_t[5,], col = "red")
    
    lines(seq(0, 1200, length.out = 10000), int_t[6,], col = "brown")
    
  }
  else{
    
    plot(seq(0, 1, length.out = 10000), int_t[1,], type = "l", col = "purple", xlim = c(0, 1), ylim = c(minval, maxval), main = paste("Object ", objid, " Interpolated Light Curve", sep=""), xlab = "Time (days)", ylab = "Flux")
    
    lines(seq(0, 1, length.out = 10000), int_t[2,], col = "blue")
    
    lines(seq(0, 1, length.out = 10000), int_t[3,], col = "green")
    
    lines(seq(0, 1, length.out = 10000), int_t[4,], col = "orange")
    
    lines(seq(0, 1, length.out = 10000), int_t[5,], col = "red")
    
    lines(seq(0, 1, length.out = 10000), int_t[6,], col = "brown")
    
  }
  
}