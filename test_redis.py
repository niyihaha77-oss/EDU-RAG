import os

import redis

# 连接到 Redis
# 密码从环境变量 REDIS_PASSWORD 读取，避免明文写进代码仓库
# 让 Redis 返回的数据自动从 bytes 解码成 Python 的 str（字符串）
client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True,
)

# 测试读写
client.set("test_key", "Hello, Redis!")
value = client.get("test_key")
print(f"Redis value: {value}")