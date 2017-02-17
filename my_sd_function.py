
# coding: utf-8

# In[55]:

# 定義自訂函數
def my_std(input_list):
    def my_length(input_list):
            '計算個數'
            temp_length = 0
            for i in input_list:
                temp_length += 1
            return temp_length
    def my_mean(input_list):
        '計算平均數' # docstrings
        def my_sum(input_list):
            '計算總和'
            temp_sum = 0
            for i in input_list:
                temp_sum += i
            return temp_sum
        return my_sum(input_list) / my_length(input_list)
    
    variance = 0
    for i in input_list:
        variance += (i - my_mean(input_list))**2     
    
    variance /= my_length(input_list)
    
    return variance**0.5
    # 呼叫自訂函數
a_list = [1, 2, 3, 4]
print(my_std(a_list))

