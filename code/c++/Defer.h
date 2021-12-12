/**
 * @file Defer.h
 * @author yuanquan (yuanquan2011@qq.com)
 * @brief @deprecated
 * 受文章《C++ RAII实现golang的defer》
 * (https://mp.weixin.qq.com/s/7Jt8oazKsIQJJTmS3UwU0w）的启发，编写一个基于C++11的defer。
 * @version 0.1
 * @date 2021-12-05
 * 
 * @copyright Copyright (c) 2021
 * 
 */

/**
 * @brief @deprecated
 * 		std::shared_ptr<void> is a better solution in C++, discuss in boost:
 * 	http://www.boost.org/doc/libs/1_59_0/libs/smart_ptr/sp_techniques.html#handle
 * for example:
 * 		shared_ptr<void> guard(nullptr, [](...){cout << "guard last" << endl;});
 * 
 * only before C++11
 * 延迟释放资源。类似于std::lock_guard
 * 利用C++RAII特性，当此类出作用域析构时，进行对应的资源释放。
 * 避免函数很多中途return时，忘记释放堆资源。
 * 
 * @tparam DeferFunc 释放资源的函数具体实现，一般应为匿名函数。
 */
template<typename DeferFunc>
class CDefer
{
public:
	CDefer(DeferFunc func)
	: m_deferFunc(func)
	{}

	~CDefer()
	{
		m_deferFunc();
	}

private:
	DeferFunc m_deferFunc;
};
