# coding=UTF-8
import configparser


# 读取配置文件
def gain_config():
    config = configparser.ConfigParser()
    config.read('properties.conf', encoding='utf-8')
    return config


# 读取配置下标index
def gain_config_index():
    index_test = gain_config().get('index', 'str_index').replace(',', '')
    index_test = set(index_test)
    return sorted(list(index_test))


# 读取配置文件的名字
def gain_config_file_name():
    file_name = gain_config().get('file', 'file_name')
    return file_name


# 切割字符串
def slicing_str(file_name):
    list_test = []
    str_test = gain_config_index()
    flag = 0
    with open('data/{}'.format(file_name), 'r', encoding='UTF-8') as f:
        with open('result/result.txt', 'w', encoding='UTF-8') as s:
            for i in f:  # 遍历指定文件的数据
                for x in i:  # 遍历每条数据
                    list_test.append(x)
                    for j in str_test:  # 遍历切割配置文件
                        if flag == int(j) - 1:  # 符合条件时切割
                            list_test.append("|")
                            str_test.remove(j)
                        flag = flag + 1
                        break
                for v in list_test:  # 输出到结果文件
                    s.write(v)
                # 处理完一条数据之后初始化变量
                list_test = []
                str_test = gain_config_index()
                flag = 0


if __name__ == '__main__':
    slicing_str(gain_config_file_name())
