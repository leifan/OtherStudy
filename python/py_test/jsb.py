play = input("请输入剪刀(0)石头(1)布(2)：")

player = int(play)

com = 1

if (player==0 and com==2) or (player==1 and com==0) or (player==2 and com==1):
	print("你赢了，真厉害")
elif player==com:
	print("平局，再来一次")
elif (player==0 and com==1) or (player==1 and com==2) or (player==2 and com==0):
	print("你输了，不要走，决战到天亮")
else :
	pass