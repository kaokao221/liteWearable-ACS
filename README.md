# liteWearable App Store, Communitee and Self Sign Platform 官方API开发文档
#### 版本目录

版本号|发布时间|URL|主要改动
-|-|-|-
[v0.1 beta](#v0.1 beta)|<还没有开始运行>|`http://api.lwacs.miniteam.com.cn/`|-

## v0.1 beta

### 账号管理
#### 注册新账号
- URL: `http://api.lwacs.miniteam.com.cn/createAccount`
- 提交方法: `GET`
- 需要的参数: 

参数名称|类型|解释|示例
-|-|-|-
`UUID`|`text`|设备UUID|`1234567890ABCDEFG`

正常的返回值:
```json
{
    "uid":"0123abcd"
}
```
