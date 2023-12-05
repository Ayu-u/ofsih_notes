# ChatGPT项目prompt整理

## 项目初始化

1.项目搭建prompt

```
请使用vue2搭建一个前端h5项目，项目名称为“heima-interview”，并配置移动端适配。
```

2.引入组件库prompt

```
请在项目中引入vant组件库，需要安装2.x版本的，并配置按需加载。
```

3.配置路由prompt

```
在项目中配置下路由，注意版本适配，需要安装vue-router3.x版本的
```

4.axios封装prompt

```
请封装下axios相关的配置，包括鉴权还有登录拦截，baseUrl为“http://interview-api-t.itheima.net/”
```



## 登录&注册

1.添加路由prompt

```
请添加下登录页面和注册页面的路由
```

2.注册页面prompt

```
请实现下注册页面，功能如下： 
1.顶部有一个导航栏，标题为“面经注册”；
2.页面中有一个表单，表单中有“用户名”和“密码”两个元素，另外还有一个提交按钮；
3.表单右下方还有个小提示，提示内容为“有账号，去登录”，点击后会跳转登录页面；
功能的实现尽量依赖vant提供的组件
```

3.注册功能prompt

```
请完善下注册函数，注册的接口地址为“/h5/user/register”，请求方法为post，参数有两个，username和password，分别对应用户名和密码，注册成功后需要跳转到登录页面
```

4.登录页面prompt

```
请实现下登录页面，页面功能和注册页面一样
```

5.登录功能prompt

```
请完善下登录函数，登录的接口地址为“/h5/user/login”，请求方法为post，参数有两个，username和password，分别对应用户名和密码，成功后需要将服务器返回的token存储到本地，然后跳转到首页
```



## 首页布局

1.首页prompt

```
请按以下要求实现首页的布局：
首页是一个一级页面，页面内容有两块，上面部分展示以下四个二级页面的内容，分别是“面经”，“收藏”，“喜欢”和“我的”，底部是一个tab栏，用vant的tabbar组件实现，一共有四个tab，分别对应前面的四个二级页面，并且点击对应的tab就会跳转到对应的页面，默认是面经页面，还需要实现这几个页面的路由的配置，项目打开时默认会跳转到首页
```



## 面经页面

1.面经页面布局prompt

```
请实现下面经页面的布局，面经页面包含两个部分：
首先页面头部的左边有两个可点击的选项，分别是“推荐”和“最新”，右边是项目的logo，头部固定在页面顶部。
然后是面经的列表，这个列表是一个无限滚动列表，使用vant组件实现，列表每一项的内容是从服务器上请求的数据
```

2.面经列表请求prompt

```
获取面经列表的接口地址为“h5/interview/query”，请求方式为get，参数有三个：
1.current，表示请求第几页的数据；
2.pageSize，表示每页多少条数据，默认给10；
3.sorter，如果在推荐栏，则传weight_desc，如果在最新栏，则不传 
每次切换tab需要重新请求数据，如果滚动到底部，自动请求下一页数据，直到最后一条，请用vant的list组件实现下获取数据的逻辑
```

3.面经组件实现prompt

```
面经文章列表中返回的每条面经的数据包括作者的名称和头像，发布时间，还有面经的标题和内容，以及点赞量和浏览量，请实现一个InfoWrapper组件来展示这些内容
```



## 收藏（喜欢）页面

1.收藏页面prompt

```
请实现下收藏页面：
页面顶部是一个导航栏，标题是”我的收藏“，导航栏固定在页面顶部，页面是一个无限滚动列表，能拉取所有的收藏的面经，每个面经的展示可以用之前封装的InfoWrapper组件，接口地址为“/h5/interview/opt/list”，参数有三个，分别是“page”，“pageSize”和“optType”，其中“optType”的值为1表示请求的收藏的面经的数据
```

> 喜欢页面一样，“optType”的值需要改为2



## 我的页面

1.个人信息展示prompt

```
请实现“我的”页面，进入页面时会请求个人信息，接口地址为“h5/user/currentUser”，包括头像和用户名，然后将这部分信息展示在页面上
```

2.跳转部分prompt

```
个人信息展示区域下面会有三个跳转的链接，分别是“历史记录”，“我的收藏”和“我的点赞”，三个链接水平分布，并且都需要添加一个额外的图标展示，可以使用vant的图标，请实现这部分代码
```

3.卡片实现prompt

```
跳转链接区域下面是一个列表，这个列表中有四个元素，分别是“推荐分享”，“意见反馈”，“关于我们”和“退出登录”，点击前三个分别会跳转到对应的页面，点击退出登录会清除存储的token，然后跳转登录页，可以用单元格组件实现
```



# ChatGPT项目prompt整理

## 登录

1.页面对象封装prompt

```
根据以下需求，针对登录页面生成UI自动化测试脚本，要求使用Python+Selenium+PO模式技术，
文件命名为login_page.py：
1. 打开登录页面，登录页面网址为：http://hmshop-test.itheima.net/Home/user/login.html
2. 输入用户名：13012345678
3. 输入密码：123456
4. 输入验证码：8888
5. 点击登录按钮登录
```



2.编写测试用例prompt

```
针对上面的登录页面，请使用Pytest生成测试脚本，如果新打开页面的标题包含“我的账户”表示登录成功。
要求单独保存到一个文件中，文件命名为test_login.py。
```





## 搜索商品

1.页面对象封装prompt

```
根据以下需求，针对首页页面生成UI自动化测试脚本，要求使用Python+Selenium+PO模式技术，
文件命名为index_page.py：
1. 打开首页页面，首页网址为：http://hmshop-test.itheima.net
2. 在首页搜索框中输入：小米手机
3. 点击搜索按钮
```



2.编写测试用例prompt

```
针对上面的首页页面，请使用Pytest生成测试脚本，如果搜索出来的商品名称中包含“小米手机”表示搜索成功。
要求单独保存到一个文件中，文件命名为test_index.py。
```





## 加入购物车

1.页面对象封装prompt

```
已知商品详情页（网址：http://hmshop-test.itheima.net/Home/Goods/goodsInfo/id/104.html），请针对该页面生成UI自动化测试脚本，具体要求如下：
1.使用Python+Selenium+PO模式技术
2.文件命名为goods_page.py
3.点击‘加入购物车’按钮
```



2.编写测试用例prompt

```
针对上面的商品详情页面，请使用Pytest生成测试脚本，具体要求如下：
1.生成的脚本单独保存到一个文件中，文件命名为test_goods.py
2.商品名称应包含“小米手机5”
3.商品商城价等于399.00元
4.页面提示：添加成功
```



# 项目Prompt

## 基于ChatGPT实现数仓构建

```properties
1、请简述网络打车日志数据的大数据开发流程
2、基于以上的日志数据，设计一个数仓分层，要求为4层
3、根据以上信息，将数仓分为：cx_ods层，cx_dwd层，cx_dwm层,cx_app层，请根据分层写出创建数据库语句
```



## 基于ChatGPT实现数仓分析

###  问题1-DWD层构建-数据清洗-订单表

```properties
Prompt:
打车订单表如下，请根据需求，完成数据清洗：
create table if not exists cx_ods.t_user_order(
	orderId string comment '订单id',
	telephone string comment '打车用户手机',
	lng string comment '用户发起打车的经度',
	lat string comment '用户发起打车的纬度',
	province string comment '所在省份',
	city string comment '所在城市',
	es_money double comment '预估打车费用',
	gender string comment '用户信息 - 性别',
	profession string comment '用户信息 - 行业',
	age_range string comment '年龄段（70后、80后、...）',
	tip double comment '小费',
	subscribe int comment '是否预约（0 - 非预约、1 - 预约）',
	sub_time string comment '预约时间',
	is_agent int comment '是否代叫（0 - 本人、1 - 代叫）',
	agent_telephone string comment '预约人手机',
	order_time string comment '预约时间'
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' ;

清洗条件如下：
1、过滤掉order_time长度小于8的数据，如果小于8，表示这条数据不合法，不应该参加统计。
2、将一些数字表示的字段，处理为更容易理解的字段。
 2.1 增加subscribe_name字段，对subscribe字段进行解释。
 2.2 增加is_agent_name字段， 对is_agent字段进行解释。
3、将所有的日期字段sub_time、order_time,进行格式转换：
      如将2020-4-12 1:15 转为 2020-04-12 01:15:00,所有日期长度是一样的。
4、从order_time中进行拆分，增加年、月、日、小时四个字段，方便后续分析。
5、增加时间段字段，时间段的划分规则如下：
	凌晨(01:00-05:00)
	早上(05:00-08:00)
	上午(08:00-11:00)
	中午(11:00-13:00)
	下午(13:00-18:00)
	晚上(18:00-22:00)
	深夜(22:00-24:00)


根据以上需求，对t_user_order表进行数据清洗，按照order_time的 年-月-日 进行分区，写出清洗的Hive SQL，
并在cx_dwd层创建目标表t_user_order_wide，该表为分区表，分区字段名为dt，字符串类型，将清洗结果插入到目标表
```

### 问题2-DWD层构建-数据清洗-订单取消表

```properties
Prompt:
以下是订单取消表，请按照规则对该表进行清洗转换
create table if not exists cx_ods.t_user_cancel_order(
    orderId string comment '订单ID',
    cstm_telephone string comment '客户联系电话',
    lng string comment '取消订单的经度',
    lat string comment '取消订单的纬度',
    province string comment '所在省份',
    city string comment '所在城市',
    es_distance double comment '预估距离',
    gender string comment '性别',
    profession string comment '行业',
    age_range string comment '年龄段',
    reason int comment '取消订单原因（1 - 选择了其他交通方式、2 - 与司机达成一致，取消订单、3 - 投诉司机没来接我、4 - 已不需要用车、5 - 无理由取消订单）',
    cancel_time string comment '取消时间'
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' ;

清洗转换规则：
1、添加reason_name字段，对reason字段进行解释
2、cancel_time字段使用date_format(concat(cancel_time,':00'),'yyyy-MM-dd HH:mm:ss') as cancel_time 使用该清洗规则 ,
3、实现以上规则的HiveSQL，并在cx_dwd层创建结果表t_user_cancel_order_wide，存储格式使用默认，，该表是分区表，分区字段是dt，
类型是string，按照cancel_time的 年-月-日 进行分区，并将清洗结果存入该表

```

### 问题3-DWD层构建-数据清洗-订单支付表

```properties
Prompt:
1、添加has_coupon_name字段，对has_coupon字段进行解释
2、添加pay_way_name字段，对pay_way字段进行解释
3、将pay_time字段按照FROM_UNIXTIME(UNIX_TIMESTAMP(order_time, 'yyyy-M-dd H:mm'), 'yyyy-MM-dd HH:mm:ss') as pay_time 规则进行转换。
4、 使用该清洗规则实现以上规则的HiveSQL，并在cx_dwd层创建结果表t_user_cancel_order_wide，该表是分区表，分区字段是dt，
类型是string，按照pay_time的 年-月-日 进行分区，并将清洗结果存入该表
```



### 问题4-DWD层构建-数据清洗-订单评价表

```properties
Prompt:
以下是用户评价表，请按照规则对该表进行清洗转换
create table if not exists cx_ods.t_user_evaluate(

清洗转换规则：

1、eva_time字段使用FROM_UNIXTIME(UNIX_TIMESTAMP(order_time, 'yyyy-M-dd H:mm'), 'yyyy-MM-dd HH:mm:ss')   as eva_time,使用该清洗规则 ,
3、实现以上规则的HiveSQL，并在cx_dwd层创建结果表t_user_evaluate_wide，该表是分区表，分区字段是dt，
类型是string，按照eva_time的 年-月-日 进行分区，并将清洗结果存入该表
```



### 问题5-DWM层构建-数据预聚合

```properties
prompt:
将以上的四张表进行 left join
t_user_pay_order_wide
t_user_cancel_order_wide,
t_user_evaluate_wide,
t_user_order_wide

2、join规则：其他三张表都和t_user_order_wide进行left join

3、join之后进行字段挑选，字段挑选的指标参考
-- 1、统计预约和非预约的订单量
-- 2、统计每天每个时段的订单统计
-- 3、统计每天,每个年龄段，每个时段的订单统计
-- 4、统计订单量最高Top3的省份名字及订单量
-- 5、统计每天不同时间段，订单取消比例，创建表并保存结果
-- 7、统计每天所有订单中，付款的订单比例，创建表并保存结果
-- 8、统计每天所有订单中，参加评论占比，创建表并保存结果
-- 9、统计每个省的订单量

4、在cx_dwm层创建目标宽表t_user_order_result，该表为分区表，分区字段为dt,类型为string，
将join后的结果存入该表，按照order_time的 年-月-日 进行分区，
```



### 问题6-APP层构建-数据指标分析

```properties
prompt:
基于以上t_user_order_result表，进行指标统计，需求如下，请实现对应的HiveSQL
-- 1、 统计每天预约和非预约的订单量,在cx_app层创建目标表t_order_subscribe_total并保存结果



prompt:
基于以上t_user_order_result表，进行指标统计，需求如下，请实现对应的HiveSQL
-- 2、统计每天每个时段的订单统计,创建目标表并保存结果


prompt:
基于以上t_user_order_result表，进行指标统计，需求如下，请实现对应的HiveSQL
-- 3、统计每天,每个年龄段，每个时段的订单统计,创建目标表并保存结果



prompt:
基于以上t_user_order_result表，进行指标统计，需求如下，请实现对应的HiveSQL
-- 4、统计每个省的订单量,创建目标表并保存结果


prompt:
基于以上t_user_order_result表，进行指标统计，需求如下，请实现对应的HiveSQL
-- 5、统计每天每个省份订单量最高Top3城市信息,创建目标表并保存结果



prompt:
基于以上t_user_order_result表，进行指标统计，需求如下，请实现对应的HiveSQL
-- 6、统计每天不同时间段，订单取消比例，创建目标表并保存结果


prompt:
基于以上t_user_order_result表，进行指标统计，需求如下，请实现对应的HiveSQL
-- 7、统计每天所有订单中，付款的订单比例，创建目标表并保存结果


prompt:
基于以上t_user_order_result表，进行指标统计，需求如下，请实现对应的HiveSQL
-- 8、统计每天所有订单中，参加评论占比，创建目标表并保存结果

```



## 基于ChatGPT及Sqoop实现数据导出

### 问题1-ChatGPT自动生成MySQL目标表

```properties
prompt:
1、统计预约和非预约的订单量，创建目标表并保存结果：
CREATE TABLE IF NOT EXISTS cx_dwm.appointment_order_count (
    dt STRING COMMENT '日期',
    is_appointment INT COMMENT '是否预约订单',
    order_count BIGINT COMMENT '订单数量'
)
PARTITIONED BY (dt STRING);
2、统计每天每个时段的订单统计，创建目标表并保存结果：

CREATE TABLE IF NOT EXISTS cx_dwm.daily_hourly_order_count (
    dt STRING COMMENT '日期',
    hour_of_day INT COMMENT '时段',
    order_count BIGINT COMMENT '订单数量'
)
PARTITIONED BY (dt STRING);
3、统计每天、每个年龄段、每个时段的订单统计，创建目标表并保存结果：
CREATE TABLE IF NOT EXISTS cx_dwm.daily_age_hourly_order_count (
    dt STRING COMMENT '日期',
    age_range STRING COMMENT '年龄段',
    hour_of_day INT COMMENT '时段',
    order_count BIGINT COMMENT '订单数量'
)
PARTITIONED BY (dt STRING);
4、统计每个省的订单量，创建目标表并保存结果：
CREATE TABLE IF NOT EXISTS cx_dwm.province_order_count (
    dt STRING COMMENT '日期',
    province STRING COMMENT '省份',
    order_count BIGINT COMMENT '订单数量'
)
PARTITIONED BY (dt STRING);

5、统计每天每个省份订单量最高的Top3城市信息，创建目标表并保存结果：

CREATE TABLE IF NOT EXISTS cx_dwm.daily_province_top3_cities (
    dt STRING COMMENT '日期',
    province STRING COMMENT '省份',
    city STRING COMMENT '城市',
    order_count BIGINT COMMENT '订单数量'
)
PARTITIONED BY (dt STRING);

6、统计每天不同时间段的订单取消比例，创建目标表并保存结果：

CREATE TABLE IF NOT EXISTS cx_dwm.daily_hourly_cancel_ratio (
    dt STRING COMMENT '日期',
    hour_of_day INT COMMENT '时段',
    cancel_ratio DOUBLE COMMENT '取消比例'
)
PARTITIONED BY (dt STRING);

7、统计每天所有订单中付款的订单比例，创建目标表并保存结果：
sql
Copy code
CREATE TABLE IF NOT EXISTS cx_dwm.daily_payment_order_ratio (
    dt STRING COMMENT '日期',
    payment_order_ratio DOUBLE COMMENT '付款订单比例'
)
PARTITIONED BY (dt STRING);


8、统计每天所有订单中参加评论的占比，创建目标表并保存结果：

CREATE TABLE IF NOT EXISTS cx_dwm.daily_comment_participation_ratio (
    dt STRING COMMENT '日期',
    comment_participation_ratio DOUBLE COMMENT '评论参与率'
)
PARTITIONED BY (dt STRING);


根据以上每个Hive表创建对应的MySQL表

```

### 问题2-ChatGPT自动生成Sqoop导出语句

```properties
prompt:
1、根据以上Hive表和对应的MySQL表，生成每个Hive表导出到MySQL表的Sqoop命令
2、模板如下：
sqoop export \
--connect "jdbc:mysql://192.168.88.100:3306/cx_app?useUnicode=true&characterEncoding=utf-8" \
--table t_order_subscribe_total \
--username root \
--password 123456 \
--hcatalog-database cx_app \
--hcatalog-table t_order_subscribe_total \
--input-fields-terminated-by '\t' \
-m 1
```

## 解决疑问并多轮提问Prompt

### 问题一：消息队列

```properties
Prompt:
ActiveMQ与Kafka有什么区别?
```

### 问题二：消息队列

```properties
Prompt:
我现在要做一个电商系统，用哪个更合适?
```

### 问题三：消息队列

```properties
Prompt:
多少吞吐量用ActiveMQ，多少吞吐量用Kafka呢?
```

### 问题四：消息队列

```properties
Prompt:
能不能给我一个大概的范围呢?
```

### 问题五：javabean

```properties
Prompt:
domain 和pojo有什么区别呢?
```

### 问题六：javabean

```properties
Prompt:
能不能给个例子？
```

## 写文档Prompt

### 问题一：写接口文档

```properties
给这个项目，https://github.com/xustudyxu/reggie_take_out.git，写一个接口文档
```

### 问题二：写部署文档

```properties
在写一个部署文档
```

## 基于ChatGPT实现数仓分析

###  问题1：创建表

```properties
Prompt:
帮我设计一张后台管理系统的用户信息表，用于登录功能
```

### 问题2：创建表

```properties
Prompt:
给username加上索引
```

### 问题3：创建表

```properties
Prompt:
插入三条数据
```

### 问题4：登录功能开发

```properties
Prompt:
按照上述表结构，帮实现代码，代码要求如下：
1, 要有控制器，控制器有登录接口实现，接口返回的类似是Result统一接口返回类
2, 要有服务层类，登录的代码在此实现，代码是注意事项如下：
        - 数据库中密码字段进行MD5加密处理
        - 登录成功，将用户id存入Session，并返回登录成功
3, 要有持久层，用mybatis实现
```

### 问题5：登录功能开发

```properties
Prompt:
补充完成上述代码中用到的实体类、UserMapper.xml、pom.xml需要导入的依赖
```

### 问题6：登录功能开发

```properties
Prompt:
上述Result是一个通用的前后端接口数据封装类，请生成完整代码
```

### 问题7：拦截功能开发

```properties
Prompt:
结合上述登录功能，写一个过滤器，实现未登录的用户拦截，具体逻辑如下：
1, 如果是登录接口则排查拦截
2, 如果登录则放行
	判断是否登录的方式如下：从session中获取userid，
	如果为null表示未登录。
	如果不为null，表示已登录
3, 如果未登录则返回未登录的结果
```

### 问题8：拦截功能开发

```properties
Prompt:
如果拦截未生效，再追问：上面的代码未生效，还需要配置什么吗？
```

### 问题9：登出功能开发

```properties
Prompt:
基于上述登录功能代码，实现登出接口开发，要求如下：
1, 请求地址为/employee/logout，请求方式为POST
2, 只需要在Controller中创建对应的处理方法即可，实现逻辑如下：
     清理Session中的用户id
     返回登出成功
```

### 问题10：员工功能开发

```properties
Prompt:
现在要完成员工新增的功能，新增的信息包括:
	id 、账号名、密码、员工姓名、手机号、性别、身份证号、账号有效状态信息，还包括创建时间、更新时间。
帮我生成创建表的sql，并给username创建一个索引
```

### 问题11：员工功能开发

```properties
Prompt:
现在帮编写新增用户的实现代码，控制层要求如下：
1、前端以json方式发送数据到服务端
2、新增用户的请求URL是/employee，请求方式POST
3、前端提交的所有数据，用Employee对象去接收
4、并把Employee对象传递给服务层
```

### 问题12：员工功能开发

```properties
Prompt:
继续实现服务层的代码，实现要求如下：
1、接收controller中传递的参数
2、新增员工的数据中，账号名、员工姓名、手机号、身份证号是必填项。
      而且手机号码和身份证号码需要用正则表达式验证
3、员工的密码默认为手机号，需要用md5进行加密
4、将新增的员工对象传递给持久层

```

### 问题13：员工功能开发

```properties
Prompt:
继续实现持久层的代码，实现要求如下：
1、持久层接口中需要用新增员工的方法
2、在EmployeeMapper.xml中完成添加员工的sql语句
```

### 问题14：时间字段自动填充

```properties
prompt: 
	使用springboot的AOP，实现对应Mapper的add开头的方法进行前置拦截，拦截后实现一下业务逻辑：
1、判断插入的对象是否存在createdTime、updatedTime、accountStatus字段
2、如果有则把对应字段设置成当前时间，否则不做任何处理
```

### 问题15：全局异常类处理

```properties
prompt: 
	用springboot的方式实现一个springmvc的全局异常增强类，统一拦截Exception异常，并返回Result类，提示信息为服务器忙，请稍后重试
```

### 问题16：员工列表功能

```properties
prompt: 
	现在实现用户列表分页查询，实现的需求如下：
1、Controller接收前端传入的page、pageSize、name参数
2、接口地址/employee/page，请求方式GET
3、数据查询在Service中实现，并且分页使用插件实现
4、接口返回Result，其中包括的数据要含总条数，和当前分页用户数据
```





## 车型识别引导词

【项目流程】

1.假设您是一名图像算法工程师,要完成一项车型识别任务,请简单描述下需要的步骤?

【数据集获取】

1.请描述下车型识别数据集获取的方式有哪些?

【图像增强】

1..请使用python代码实现车型图像的几何增强和颜色增强?

【模型构建】

1.请使用pytorch构建一个resnet34的模型完成1778类的车型识别任务?

【模型训练】

1.请使用python实现使用车型训练集数据训练resnet34模型的代码?

【模型预测】

1.请利用上述训练好的模型参数,编写python代码实现模型预测

【模型部署】

1.请使用flask框架实现车型识别模型的部署代码?

2.请使用python代码实现客户端代码?

