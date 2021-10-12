# Effictive C++

## 概要

对数据《Effective C++：改善程序与设计的55个具体做法》的读书摘要。

## Item 1： 将 C++ 视为 federation of languages（语言联合体）

C++是一个多范式编程语言（multiparadigm programming language），包括：

- 面向过程（procedural）
- 面向对象（object-oriented）
- 函数式编程（functional）
- 泛型及元编程（generic and metaprogramming）

effective C++ programming（高效C++编程）规则的变化，依赖于使用的C++的哪个部分。

## Item 2：用consts，enums和inlines取代#defines

即用编译器（compiler）取代预处理器（preprocessor）。

- 对简单常量（simple constants），用const 对象（const objects）或枚举（enums）取代#defines；

- 对函数宏（function-like macros），用内联函数（inline functions）取代#defines；

## Item 3：只要可能就用const

- 将某些东西声明为const有助于编译器发现使用错误。const能被用于任何scope（作用域）中的object（对象），用于function parameters（函数参数）和return types（返回类型），用于整个member functions（成员函数）；
- 编译器坚持bitwise constness（二进制位常量性），但是你应该用conceptual constness（概念上的常量性）来编程；
- 当const和non-const member functions（成员函数）具有本质上相同的实现的时候，使用non-const版本叫用const版本可以避免代码重复（code dumplication）；

## Item 4：确保对象（objects）在使用前被初始化

- 手动初始化内建类型（built-in type）的对象（objects），因为C++只在某些时候才会自己初始化它们；
- 在构造函数（constructor）中，用成员初始化列表（member initialization list）代替函数体中的赋值（assignment）。初始化列表（initialization list）中数据成员（data members）的排序顺序要与它们在类（class）中被声明的顺序相同；
- 通过用局部静态对象（local static objects）代替非局部静态对象（non-local static objects）来避免跨转换单元（translation units）的初始化顺序问题（initialization order problems）；

## Item5：了解C++为你偷偷地加上和调用了什么函数

- 编译器隐式生成了类的缺省构造函数（default constructor）、拷贝构造函数（copy constructor）、拷贝赋值运算符（copy assignment operator）、析构函数（destructor）；

## Item6：如果你不想使用compiler-generated functions（编译器生成函数），就明确拒绝

- 为了拒绝编译器自动提供的机能，将相应的成员函数（member functions）声明为private（C++11，delete），而且不要实现。

## Item7：在多态基类（polymorphic base classess）中，将析构函数（destructors）声明为virtual

- 多态基类（polymorphic base classes）应该声明虚拟析构函数（virtual destructor）。如果一个类有任何虚拟函数，就应该有虚拟析构函数；
- 不是设计用来用作基类或不是设计用于多态的类，就不应该声明为虚拟析构函数；

## Item8：防止因为异常离开析构函数

- 析构函数应该永不引发异常。如果析构函数调用了可能抛出异常的函数，析构函数应该捕捉所有异常，然后抑制它们或者终止程序。
- 如果类的使用者需要能对一个操作抛出的异常做出回应，则该类应该提供一个常规函数，来完成该操作。

## Item9：绝不要在构造或析构期间，调用虚拟函数

- 在构造或析构期间，不要调用虚拟函数。因为这样的调用，不会转到比当前执行的构造或析构函数所属类更深层的派生类。

## Item10：让赋值运算符（assignment operators）返回一个指向*this的引用（reference to *this）

- 让赋值运算符（assignment operator）返回一个指向*this的引用（reference to *this）；

## Item11：在operator=中处理字符值（assignment to self）

- 当一个对象被赋值给自己的时候，确保operator=是行为良好的。技巧包括比较源（source）和目标对象（target objects）的地址，关注语句顺序，和copy-and-swap；
- 如果两个或更多对象（objects）相同，确保任何操作多于一个对象的函数行为正确；

## Item12：拷贝一个对象的所有组成部分

-  拷贝函数应该保证拷贝一个对象的所有数据成员以及所有的基类部分；
- 不要试图依据一个拷贝函数实现另一个。作为替代，将通用功能放入第三个供双方调用的函数；

## Item13：使用对象管理资源

- 为了防止资源泄露，使用RAII对象，在RAII对象的构造函数中获取资源并在析构函数中释放它们；
- 两个通用的RAII是tr1::shared_ptr和auto_ptr。tr1::shared_ptr通常是更好的选择，因为它拷贝时的行为是符合直觉的。拷贝一个auto_ptr是将它置为空。

## Iteam14：谨慎考虑资源管理类的拷贝行为

- 拷贝一个RAII对象必须拷贝它所管理的资源，所有资源的拷贝行为决定了RAII对象的拷贝行为；
- 普通的RAII类的拷贝行为不接受拷贝和进行引用计数，但是其他行为是有可能的；

## Item15：在资源管理类中准备访问裸资源（raw resources）

- API经常需要访问裸资源，所以每一个RAII类都应该提供取得它所管理资源的方法；
- 访问可以通过显示转换或者隐式转换进行。通常，显示转换更安全，而隐式转换对客户来说更方便；

## Item16：使用相同形式的new和delete

- 如果你在new表达式中使用了[]，你必须在对应的delete表达式中使用[]；如果你在new表达式中没有使用[]，你也不要在对应的delete表达式中使用[]。

## Item17：在一个独立的语句中将new出来的对象存入智能指针

- 在一个独立的语句中将new出来的对象存入智能指针。如果疏忽这点，当发生异常时，可能引起资源泄露；

## Item18：使接口易于正确使用，而难以错误使用

- 好的接口易于正确使用，而难以错误使用。你应该在所有的接口中为这个特性努力；
- 是易于正确使用的方法包括在接口和行为兼容性上与内建类型保持一致；
- 预防错误的方法包括创建新的类型，限定类型的操作，约束对象的值，以及消除客户的资源管理职责。
- tr1::shared_ptr支持自定义deleter。这可以预防cross-DLL问题，能用于自动解锁互斥体；

## Item19：视类设计为类型设计

- 类设计就是类型设计。定义一个新类型之前，确保考虑了如下问题：
  1. 如何创建和销毁；
  2. 初始化和赋值的不同；
  3. 值传递的含义；
  4. 合法值的限定条件；
  5. 继承图表；
  6. 类型转换；
  7. 有意义的运算符和函数；
  8. 那些标准函数应delete；
  9. 成员的访问；
  10. 未声明接口，性能、异常安全、资源使用；
  11. 通用性；
  12. 真的需要？是否可继承；

## Item20：用传const引用（pass-by-reference-to-const）取代传值（pass-by-value）

- 用传引用给const取代传值，通常，更高效且可避免切断问题；
- 此规则不适用于内建类型、STL中的迭代器和函数对象类型。

## Item21：当你必须返回一个对象时不要试图返回一个引用

- 不要返回局部栈对象的指针或引用；不要返回内部分配的堆对象的引用；如果需要多个对象时，不要返回局部static对象的指针或引用；

## Item22：将数据成员声明为private

- 声明数据成员为private；
- protected并不比public的封装性强；

## Item23：用非成员非友元函数取代成员函数

- 用非成员非友元函数取代成员函数。这样可以提高封装性、包装弹性和技能扩充性；

## Item24：当类型转换应该用于所有参数时，声明为非成员函数

- 如果函数的所有参数使用了类型转换，该函数必须是非成员函数

## Item25：考虑支持不抛异常的swap

- 如果std::swap对自定义类型是低效的，请提供一个swap成员函数，并确保swap不会抛出异常；
- 如果提供了一个成员swap函数，请同时提供一个调用成员swap的非成员swap。对于类，还要特化std::swap；
- 确保自己调用的std::swap，或自声明的swap；
- 为用户定义类型完全特化std模板没问题，但不要加入std；

## Item26：只要有可能，就推迟变量定义

- 尽量推迟变量定义，可增加程序的清晰度并提高性能；

## Item27：将强制转换减到最少

- 避免类型的强制转换；
- 如果必须，设法隐藏在一个函数中；
- 使用C++风格强制转换，替换旧风格的强制转换；

## Item28：避免返回对象内部构件的”句柄“

- 避免返回对象内部构件（引用、指针或迭代器）；

## Item29：正确异常安全（exception-safe）的代码

- 当有异常时，异常安全的函数，不会泄露资源，也不允许数据结构恶化。此类函数提供基本的、强力的，或不抛异常的保证；
- 强力保证经常可以通过copy-and-swap被实现，但是强力保证并非对所有函数可用；
- 一个函数能提供的保证，通常不会强于所调用函数的最弱保证；

## Item30：理解inline化的介入和排除

- 将inline限制在短小、调用频繁的函数上；
- 不要因为函数模板在头文件中，就声明为inline；

## Item31：最小化文件之间的编译依赖

- 最小化编译依赖，一般时用对声明的依赖取代对定义的依赖。一般使用Handle类和Interface类；
- 库文件应该以完整且只有声明的形式存在，无论是否包含模板；

## Item32：确保public inheritance模板is-a

- 公有继承意味着is-a。适用于base classes的每一件事，也适用于derived classes；

## Item33：避免覆盖（hiding）通过继承得到的名字

- derived classes中的名字覆盖base classes中的名字，在public inheritance中，绝非如此；
- 为使隐藏的名字重新可见，使用using declaration或forwarding functions（转调函数）；

## Item34：区分接口继承（inheritance of interface）和实现继承（inheritance of implementation）

- 接口继承与实现继承不同。在公开继承下，派生类总是继承基类接口；
- 纯虚函数指定接口继承；
- 简单虚函数指定接口继承，且缺省实现继承；
- 非虚函数指定接口继承，加上强制实现继承；

## Item35：考虑可选的虚拟函数的替代方法

- 虚拟函数替代方法：NVI惯用法（非虚拟接口管用法）和策略模式；

## Item36：绝不要重定义一个通过继承得到的非虚拟函数

- 绝不要重定义通过继承得到的非虚拟函数；

## Item37：绝不要重定义一个函数中，通过继承得到的缺省参数值（inherited default parameter value）

- 不要重定义一个通过继承得到的缺省参数值（inherited default parameter value），因为缺省参数值（default prameter value）是静态绑定（statically bound），而虚函数是动态绑定；

## Item38：通过复合（composition）模拟“has-a”（有一个）或"is-implemented-in-terms-of"(是根据...实现的)

- 复合（composition）与公有继承（public inheritance）的意义完全不同；
- 在应用领域，复合意味着has-a。在实现领域，复合意味着is-implemented-in-terms-of；

## Item39：谨慎使用私有继承（privated inheritance）

- 私有继承意味着is-implemented-in-terms-of，通常比复合（composition）更低级。但当派生类需要访问保护基类成员（protected base class members）或需要重定义继承来的虚函数（inherited virtual functions）时，就是合理的；
- 与复合不同，私有继承能使空基优化（empty base optimization）有效。这对致力于最小化对象大小（object sizes）的库开发者来说，可能很重要；

## Item40：谨慎使用多重继承（multiple inheritance）

- 多继承比单继承（single inheritance）更复杂。它能导致新的歧义问题和对虚函数的需要；
- 虚拟继承增加了大小（size）和速度（speed）成本，以及初始化（initialization）和赋值（assignment）的复杂度。当虚拟基类（virtual base classes）没有数据时，是最适用的；
- 多继承（multiple inheritance）有合理的用途。一种方案涉及组合从一个接口类（Interface）的公有继承，和从一个有助于实现的类的私有继承；

## Item41：理解隐式接口（implicit interfaces）和编译期多态（compile-time polymorphism）

- 类（classes）和模板（templates）都支持接口（interfaces）和多态（polymorphism）；
- 对类，接口时显示（explicit）的，并以函数识别特征（function signatures）为中心。多态性（polymorphism）通过虚拟函数（virtual functions）出现在运行期；
- 对于模板参数（template parameters），接口是隐式的（implicit），并基于合法表达式（valid expressions）。对多态（polymorphism）通过模板实例化（template instantiation）和函数重载解析（function overloading resolution）出现在编译器；

## Item42：理解typename的连个含义

- 在声明模板参数（template parameters）时，class和typename是可互换的；
- 用typename去标识嵌套依赖类型名（nested dependent type names），在基类列表（base class lists）中或成员初始化列表（member initialization list）中，作为一个基类标识符（base class identifier）时除外；

## Item43：了解如何访问模板化基类（templatized base classes）中的名字

- 在派生类模板（derived class templates）中，可以经由this->前缀，经由using declarations，或经由一个显示基类限定（explicit base class qualification）引用基类模板（base class templates）中的名字；

## Item44：从模板（template）中分离参数无关（parameter-independent）的代码

- 模板产生多个class和function，所以一些不依赖于模板参数（template paramter）的模板代码，会引起膨胀；
- 非类型模板参数（non-type template parameter）引起的膨胀，常常可以通过函数参数（functions parameter）或类数据成员（class data members）替换模板参数而消除；
- 类型参数（type parameter）引起的膨胀，可以通过让具有相同的二进制表示的实例化类型共享实现而减少；

## Item45：用成员函数模板（member function template）接受所有兼容类型（all compatible types）

- 使用成员函数模板（member function template）生成接受所有兼容类型的函数；
- 如果为泛型化拷贝构造（generalized copy construction）或泛型化赋值（generalized assignment）声明了成员模板（member template），依然需要声明

## Item46：需要类型转换（type conversion）时，在模板内定义非成员函数（non-member functions）

- 在写一个类模板时，如果这个类模板提供了一些函数，这些函数涉及到支持所有参数的隐式类型转换的模板时，把这些函数定义为类模板内部的友元

## Item47：为类型信息使用特征类（traits classes）

- traits classes 使关于类型的信息在编译期间可用，其使用模板和模板特化实现；
- 结合重载，traits class是的执行编译期类型if ... else检验成为可能；

## Item48：感受模板元编程（template metaprogramming）

- 模板元编程能将工作从运行期转移到编译期，就能更早察觉出错误，并提高运行时的性能；
- TMP能用于在policy choices的组合的基础上，生成自定义代码，也能用于避免为特殊类型生成不适当的代码；

## Item49：了解new-handler的行为

- set_new_handler允许你指定一个当内存分配请求不能被满足时，可以被调用的函数；
- nothrow new作用有限，因为仅适用于内存分配，随后的constructor调用可能依然会排除异常；

## Item50：领会何时替换new和delete才有意义

- 有很多正当的编写自定义new和delete的自定义版本的理由，包括改进性能、调试堆的错误用法，以及收集堆的用法信息；

## Item51：编写new和delete时要遵守惯例

- operator new应该包含一个设法分配内存的无限循环，如果它不能满足一个内存请求，应该嗲用new-handler，还应该处理0字节请求。类专用（class-specific）版本应该处理对比预期更大的区块请求；
- operator delete如果收到一个空指针，应该什么都不做。类专用（class-specific）版本应该处理比预期更大的区块；

## Item52：如果编写了placement new，就要编写placement delete

- 在编写一个operator new的placement版本是，确保同时编写operator delete的相应placement版本。否则，程序可能会发生微妙的、断续的内存泄露（memory leaks）；
- 当声明new和delete的placement版本时，确保不会无意中覆盖这些函数的常规版本呢；

## Item53：不要轻忽编译器的警告

- 严肃对待编译器发出的警告信息。努力在你的编译器的最高警告级别下，争取“无任何警告”的荣誉；
- 不要过度依赖编译器的报警能力，因为不同的编译器对待事情的态度并不相同。一旦移植到另一个编译器上，你原本依赖的警告信息有可能消失；

## Item54：让自己熟悉包括TR1在内的标准程序库

## Item55：让自己熟悉boost
