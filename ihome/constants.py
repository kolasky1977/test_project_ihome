# 专用于保存程序中用到的常量数据

# 图片验证码的有效期，单位：秒
IMAGE_CODE_REDIS_EXPIRES = 180

# 短信验证码的redis有效期, 单位：秒
SMS_CODE_REDIS_EXPIRES = 300

# 发送短信验证码的间隔, 单位：秒
SEND_SMS_CODE_INTERVAL = 60

# 登录错误尝试次数
LOGIN_ERROR_TIMES = 5

# 登录错误限制事件，单位：秒
LOGIN_ERROR_FORBID_TIME = 600

# 用户上传图片的保存地址域名
UPLOAD_IMAGE_URL = 'http://127.0.0.1:5000/static/images/'

# 城区信息的缓存时间，单位：秒
AREA_INFO_REDIS_EXPIRE = 7200
