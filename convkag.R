convkag <- function(data, type = "t"){
  
  library(data.table)
  
  u_band <- as.data.frame(matrix(0, nrow = nrow(data), ncol = 10000))
  
  g_band <- as.data.frame(matrix(0, nrow = nrow(data), ncol = 10000))
  
  r_band <- as.data.frame(matrix(0, nrow = nrow(data), ncol = 10000))
  
  i_band <- as.data.frame(matrix(0, nrow = nrow(data), ncol = 10000))
  
  z_band <- as.data.frame(matrix(0, nrow = nrow(data), ncol = 10000))
  
  y_band <- as.data.frame(matrix(0, nrow = nrow(data), ncol = 10000))
  
  objid <- data$object_id
  
  for (i in 1:length(objid)){
    
    if (i %% 1 == 0){
      
      print(i)
      
    }
    
    int <- fread(paste("F:/Documents/Kaggle/Results/int_", objid[i], "_", type, ".csv", sep=""), colClasses = rep("character", 10000))
    
    u_band[i,] <- int[1,]
    
    g_band[i,] <- int[2,]
    
    r_band[i,] <- int[3,]
    
    i_band[i,] <- int[4,]
    
    z_band[i,] <- int[5,]
    
    y_band[i,] <- int[6,]
    
  }
  
  write.table(u_band, file = paste("F:/Documents/Kaggle/Results/u_band_", type, ".csv", sep=""), sep=",", col.names = F, row.names = F, quote = F)
  
  write.table(g_band, file = paste("F:/Documents/Kaggle/Results/g_band_", type, ".csv", sep=""), sep=",", col.names = F, row.names = F, quote = F)
  
  write.table(r_band, file = paste("F:/Documents/Kaggle/Results/r_band_", type, ".csv", sep=""), sep=",", col.names = F, row.names = F, quote = F)
  
  write.table(i_band, file = paste("F:/Documents/Kaggle/Results/i_band_", type, ".csv", sep=""), sep=",", col.names = F, row.names = F, quote = F)
  
  write.table(z_band, file = paste("F:/Documents/Kaggle/Results/z_band_", type, ".csv", sep=""), sep=",", col.names = F, row.names = F, quote = F)
  
  write.table(y_band, file = paste("F:/Documents/Kaggle/Results/y_band_", type, ".csv", sep=""), sep=",", col.names = F, row.names = F, quote = F)
  
}


writekaggleab <- function(data){
  
  for (i in 1:length(data)){
    
    write.table(data[[i]], file = paste("F:/Documents/Kaggle/Abstractmats/kaggleabimgs_", i, ".csv", sep=""), sep=",", col.names = F, row.names = F)
    
  }
  
}