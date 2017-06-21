# coding: utf-8
import sys
from mns.account import Account
from mns.topic import DirectSMSInfo, TopicMessage
from mns.mns_exception import MNSExceptionBase
accid = 'LTAIf6atnIup14AK'
acckey = 'zfoeCi2Au0le7vUbsFOmEVtPrtlfZf'
endpoint = 'http://1771999519197750.mns.cn-hangzhou.aliyuncs.com/'
topic_name = 'sms.topic-cn-hangzhou'
my_account = Account(endpoint, accid, acckey)
my_topic = my_account.get_topic(topic_name)
'''
Step 2. 设置SMS消息体（必须）
注：目前暂时不支持消息内容为空，需要指定消息内容，不为空即可。
'''
msg_body1 = "sms-message1."
'''
Step 3. 生成SMS消息属性，single=False表示每个接收者参数不一样，
'''
# 3.1 设置SMSSignName和SMSTempateCode
direct_sms_attr1 = DirectSMSInfo(free_sign_name="宁师生活网", template_code="SMS_69460049", single=False)
# 3.2 指定接收短信的手机号并指定发送给该接收人的短信中的参数值（在短信模板中定义的）
direct_sms_attr1.add_receiver(receiver="18150850025", params={"code": "123456"})
'''
#Step 5. 生成SMS消息对象
'''
msg1 = TopicMessage(msg_body1, direct_sms=direct_sms_attr1)
try:
    '''
    Step 6. 发布SMS消息
    '''
    re_msg = my_topic.publish_message(msg1)
    print "Publish Message Succeed. MessageBody:%s MessageID:%s" % (msg_body1, re_msg.message_id)
except MNSExceptionBase, e:
    if e.type == "TopicNotExist":
        print "Topic not exist, please create it."
        sys.exit(1)
    print "Publish Message Fail. Exception:%s" % e