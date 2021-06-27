/*************************************************
 * @Description: 受文章《C++ RAII实现golang的defer》
 (https://mp.weixin.qq.com/s/7Jt8oazKsIQJJTmS3UwU0w）的启发，
 编写一个基于C++11的defer。
 * @Author: yuanquan
 * @Email: yuanquan2011@qq.com
 * @Date: 2021-06-27 12:28:33
 * @LastEditors: yuanquan
 * @LastEditTime: 2021-06-27 12:55:37
 * @copyright: Copyright (c) yuanquan
 *************************************************/

/*************************************************
 * @description: 延迟释放资源。类似于std::lock_guard
  利用C++RAII特性，当此类出作用域析构时，进行对应的资源释放。
  避免函数很多中途return时，忘记释放堆资源。
 * @param {DeferFunc} 释放资源的函数具体实现，一般应为匿名函数。
 *************************************************/ 
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
