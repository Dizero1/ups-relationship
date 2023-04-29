# ups-relationship
本项目属于课程作业，形式为py爬虫

旨在通过切片的tag来追踪不同up的关系热度，更好的分析up关系网
<details><summary>更好的</summary>磕cp : )</details>
<details>
<summary>video.stat内容:</summary>

| 字段    | 类型  | 内容   | 备注    |
|---------|-----|------|------------------------------------------------------------------------------------|
| code    | int | 返回值  | 0：成功<br />-400：请求错误<br />-403：权限不足<br />-404：无视频<br />62002：稿件不可见<br />62004：稿件审核中 |
| title   | str | 稿件标题     |                                                    |
| bvid    | str | 稿件bvid     |                                                    |
| aid     | int | 稿件avid     |                                                    |
| up_uid  | int | UP主uid      |       |
| up_name | str | UP主昵称     |       |
| view    | int | 播放数       |       |
| danmaku | int | 弹幕数       |       |
| reply   | int | 评论数       |       |
| favorite | int | 收藏数      |       |
| coin    | int | 投币数       |       |
| like    | int | 获赞数       |       |
| tag     | list | tag列表     |       |

| 字段    | 类型  | 内容   | 备注    |
|---------|-----|------|------------------------------------------------------------------------------------|
| tag_id     | int | tagid     |       |
| tag_name   | str | tag名     |       |
</details>
