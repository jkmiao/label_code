
## 验证码在线标注打码平台
<code>原理:</code> 利用用户的输入标签, 将static/uploads 文件夹下的验证码图片重命名.

##  使用
1. 将需要打标的验证码图片复制到 ./static/uploads 文件夹下, 打完标再 mv 移走
2. 下载到本地:
3. git clone 'git@112.74.93.140:miaoweihong/label_code.git'
4. cd label_code

```python web_server.py ```

打开浏览器: http://192.168.0.170:8088/ 按照说明, 进行标注

----

![标注示例](label_code/demo_img.jpg 'demo example') 


----
>> by- miaoweihong@tungee.com
>> @2017.06
