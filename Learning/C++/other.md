# Bug and Solution

## Bug: jsoncpp的编码问题

**问题**：在项目过程中，通过jsoncpp组json字符串，发现输入字符串为UTF8编码，但输出却为GBK（应为系统区域编码）。

**解决方案**：

参考：https://stackoverflow.com/questions/50637362/how-can-i-ask-jsoncpp-to-encode-unicode-strings

依赖jsoncpp 1.9.2或以上。对json的builder，指定编码格式。代码：

```cpp
void print_json(const Json::Value& value, bool emitUTF8) {
    Json::StreamWriterBuilder builder;
    builder.settings_["emitUTF8"] = emitUTF8;
    std::unique_ptr<Json::StreamWriter> writer(builder.newStreamWriter());
    writer->write(value, &std::cout);
}
```
