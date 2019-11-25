#### Swagger字段说明

| 字段           | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| schemes        | 使用协议（如：`http`、`https`）                              |
| host           | 项目地址，这个地址会作为每个接口的`url base`，拼接起来一起作为防伪地址 |
| consumes       | 接口默认接收的`MIME`类型（如：`formData`）                   |
| produces       | 接口默认返回`MIME`类型。`api`接口用的比较多的是 `application/json` 和 `application/xml` |
| summary        | 接口的简要介绍，会显示在接口标头上，不能超过`120`个字符      |
| description    | 接口的详细介绍                                               |
| externalDocs   | 外部文档连接                                                 |
| operationId    | 全局唯一的接口标识                                           |
| parameters     | 参数列表                                                     |
| @SWG\Info      | 此项填写的内容会放在文档开头，用作文档说明                   |
| @SWG\TAG       | `tag`是用来给文档分类的，`name`字段必须唯一，某个接口可以指定多个`tag`，那它就会出现在多组分类中（`tag`也可以不用在这里预先定义） |
| @SWG\Get       | 通过`get`的方式请求数据                                      |
| @SWG\Post      | 通过`post`的方式请求数据                                     |
| @SWG\Parameter | **常用字段说明**                                             |
| name           | 参数名                                                       |
| in             | 参数的来源，必填，取值范围：`query`、`header`、`path`、`formData`、`body` |
| description    | 参数描述                                                     |
| type           | 参数类型，取值范围：`string`、`number`、`integer`、`boolean`、`array`、`file` |
| required       | 参数是否必须，取值范围：`true`、`false` (通过路径传参`in="path"`时必须为`true`) |
| default        | 参数的默认值                                                 |