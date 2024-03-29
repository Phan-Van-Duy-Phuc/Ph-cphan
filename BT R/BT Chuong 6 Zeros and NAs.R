#6.3 Function
#6.3.1. Zeros and NAs
setwd("D:\\Documents")
Veg <- read.table(file="Vegetation2.txt", header = TRUE)
names(Veg)
#Hàm kiểm tra xem trong cột có bao nhiêu biến chứa NA
NAPerVariable <- function(X1){
  D1 <- is.na(X1)
  colSums(D1)
}
NAPerVariable(Veg)
CP <- read.table(file="CodParasite.txt", header = TRUE)
NAPerVariable(CP)
#Hàm kiểm tra biến zero (0)


ZeroPerVariable <- function(X1){
  D1= (X1==0)
  colSums(D1)
}
ZeroPerVariable(Veg)
ZeroPerVariable(CP)
ZeroPerVariable <- function(X1){
  D1= (X1==0)
  colSums(D1, na.rm = TRUE)
}
ZeroPerVariable(Veg)
ZeroPerVariable(CP)


#6.3.2 Hàm có nhiều tham số
VariableInfo <-function(X1, Choice1){
  if (Choice1== "Zeros") {
    D1= (X1==0)
  }
  if (Choice1== "NAs") {
    D1 <- is.na(X1)
  }
  colSums(D1, na.rm=TRUE)
}
VariableInfo(CP,"Zeros")
VariableInfo(CP,"NAs")
VariableInfo(CP,"thamso")
VariableInfo(CP)


#6.3.3
#Gán giá trị mặc định cho Choice1
VariableInfo <-function(X1, Choice1="Zeros"){
  if (Choice1== "Zeros") {
    D1= (X1==0)
  }
  if (Choice1== "NAs") {
    D1 <- is.na(X1)
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