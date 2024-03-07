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

## CMake控制文件警告

**问题**：C++编码过程，使用protobuf，而生成.cc和.h文件，带有太多警告。导致，整个项目无法避免警告，从而，无法通过解决编译期警告，解决编译问题。

**解决方案**：CMake控制特定文件的警告。操作如下：

```cmake
set_source_files_properties(somefile.cpp PROPERTIES COMPILE_FLAGS "-w")

```

使用 `set_source_files_properties()` 函数为这两个特定的文件设置编译选项。`COMPILE_FLAGS` 是一个 CMake 属性，用于设置编译器的选项。使用 `-w` 选项来禁止警告。
