/**
 * @file Join.h
 * @author yuanquan (yuanquan2011@qq.com)
 * @brief 
 * @version 0.1
 * @date 2022-03-20
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <string>
using std::string;

template<typename OutputIter>
void SpliteString(OutputIter iter, const string& str, const string& sep)
{
	string::size_type posBegin, posEnd;
	posEnd = str.find(sep);
	posBegin = 0;
	while (string::npos != posEnd)
	{
		*iter++ = str.substr(posBegin, posEnd-posBegin);

		posBegin = posEnd + sep.size();
		posEnd = str.find(sep, posBegin);
	}

	if(posBegin != str.length())
	{
		*iter++ = str.substr(posBegin);
	}
}
template<typename Contain>
string Join(Contain c, const string& sep)
{
	string str;
	for(const auto& s : c)
	{
		str += s + sep;
	}
	if(!str.empty())
	{
		str.erase(str.end() - sep.size(), str.end());
	}
	return str;
}
