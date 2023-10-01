from db_config import Weight

user_name = input("ユーザ名を入力してください＞")
user_weight = input("ユーザの体重を入力してください＞")

weight = Weight(name = user_name, weight = user_weight)
weight.save()
print("ユーザー名と体重の登録に成功しました")

for wgt in Weight.select():
    print(f"{wgt.name}{wgt.weight}")