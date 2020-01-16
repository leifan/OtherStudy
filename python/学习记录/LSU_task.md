# LSU task

## 2020-01-16

基于版本，sam认为This program seems to be the same as the last version.  It does not give the expected results.



Adaptation Hardware Version: LLHT-US1.3 、LLHT-US1.3 .1、LLHT-US1.3 .2、LLHT-US1.3.3

PLC Software Version: US_PLC_V1.20.3_20200115LF

Display Version: US_SCREEN_V1.20.3_20190725

Version Type: Test Version









## 2020-01-15

​		

We still have problem.  When there is a Vibration Fault and an RPC Pause present, once the Vibration Switch is closed again when the reset command is given the Red Fault light turns off and the Vibration Fault message on the screen goes away, but the LAR2 does not actually close for five seconds to reset the brake.  This could lead to a situation where once the Pause signal is closed the customer tries to run the unit but the emergency brake is still set.

We need for LAR2 to close for five seconds like normal to reset the brake when the fault is cleared.  It should be this way for both the RPC Pause and VSD Pause with any Fault or multiple Fault combination.

Sam

我们还有问题。当存在振动故障和RPC暂停时，一旦振动开关再次关闭，当发出复位命令时，红色故障灯熄灭，屏幕上的振动故障信息消失，但LAR2实际上在5秒钟内不会关闭以复位制动器。这可能导致一种情况，即一旦暂停信号关闭，客户试图运行该装置，但紧急制动仍处于设定状态。


我们需要LAR2像正常一样关闭5秒钟，以便在故障清除后重置制动器。对于任何故障或多个故障组合的RPC Pause和VSD Pause都应该这样。

山姆

------

![1579056857437](D:\github\OtherStudy\python\学习记录\img\1579056857437.png)

LAR1 刹车启动

LAR2  刹车复位



修改方案： 运行条件增加刹车动作已停止时才启动。

![1579060818102](D:\github\OtherStudy\python\学习记录\img\1579060818102.png)