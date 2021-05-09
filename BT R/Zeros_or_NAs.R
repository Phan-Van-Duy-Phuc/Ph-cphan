#6.3 Function

#6.3.1. Zeros and Nas
setwd('D:\\Documents')
Veg <- read.table(file='Vegetation2.txt',header = TRUE)
names(Veg)
#Hàm kiểm tra xem trong cột có bao nhiêu biến chứa NA
NAPerVariable <- function(x1){
  D1 <- is.na(x1)
  colSums(D1)
}
NAPerVariable(Veg)
CP <- read.table(file='CodParasite.txt',header = TRUE)
NAPerVariable(CP)
#Hàm kiểm tra biến zero (0)

ZeroPerVariable <- function(x1){
  D1 = (x1==0)
  colSums(D1)
}  
ZeroPerVariable(Veg)
ZeroPerVariable(CP)
ZeroPerVariable <- function(x1){
  D1 = (x1==0)
  colSums(D1, na.rm = TRUE)
}
ZeroPerVariable(Veg)
ZeroPerVariable(CP)

#6.3.2 Hàm có nhiều tham số
#Gán giá trị mặc định cho choice1
VariableInfo <- function(x1, choice1){
  if (choice1 == "Zeros"){
    D1 = (x1==0)
  }
  if (choice1=="NAs"){
    D1 <- is.na(x1)
  }
  colSums(D1, na.rm=TRUE)
}
VariableInfo(CP,"Zeros")
VariableInfo(CP,"NAs")
VariableInfo(CP,"thamso")
VariableInfo(CP)


#6.3.3 
#Gán giá trị mặc định cho choice1


VariableInfo <- function(x1, choice1="Zeros"){
  if (choice1 == "Zeros"){
    D1 = (x1==0)
  }
  if (choice1=="NAs"){
    D1 <- is.na(x1)
  }
  colSums(D1, na.rm=TRUE)
}
VariableInfo(CP,"Zeros")
VariableInfo(CP,"NAs")
VariableInfo(CP,"thamso")
VariableInfo(CP)



#Tham số không giống với giá trị của chúng ta
#Đưa ra 1 thông báo


VariableInfo <-function(X1, Choice1="Zeros"){
  if (Choice1== "Zeros") {
    D1= (X1==0)
  }
  if (Choice1== "NAs") {
    D1 <- is.na(X1)
  }
  if (Choice1!= "Zeros" & Choice1 != "NAs") {
    print("You make a miss typo.You should choose: Zeros or NAs")
  }else{
    colSums(D1, na.rm=TRUE)
  }
}
VariableInfo(CP,"Zeros")
VariableInfo(CP,"NAs")
VariableInfo(CP,"thamso")
VariableInfo(CP)













