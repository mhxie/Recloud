# Adaptor Readme
## Interface
### add_adaptor(configdir,adaptor_type)
新增加一个adaptor, 参数为配置文件目录和适配器类型

### del_adaptor(configdir)
删除adaptor的配置文件目录,删除之后此adaptor无法继续使用

### class adaptor(num_of_adaptor)
参数是adaptor编号，返回对一个Object
### adaptor 成员函数
1. adaptor::upload
2. adaptor::download
3. adaptor::delete
4. adaptor::info

### 配置文件目录
所有配置文件均存在 ./config里面

### 具体使用可以看adaptor.py 里面的sample
