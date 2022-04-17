/**
 * @file log.h
 * @author yuanquan (yuanquan2011@qq.com)
 * @brief a log based on boost.log
 * 		depend: boost.log.v2
 * @version 0.1
 * @date 2021-12-11
 * 
 * @copyright Copyright (c) 2021
 * 
 */

#include <fstream>
#include <string>
#include <mutex>
#include <boost/smart_ptr/shared_ptr.hpp>
#include <boost/smart_ptr/make_shared_object.hpp>

#include <boost/log/common.hpp>
#include <boost/log/expressions.hpp>
#include <boost/log/sources/logger.hpp>

#include <boost/log/utility/setup/file.hpp>
#include <boost/log/utility/setup/console.hpp>
#include <boost/log/utility/setup/common_attributes.hpp>
#include <boost/thread/thread.hpp>

#include <boost/log/support/date_time.hpp>
#include <boost/log/attributes/named_scope.hpp>
#include <boost/log/attributes/timer.hpp>
#include <boost/log/attributes/current_process_id.hpp>
#include <boost/log/attributes/current_process_name.hpp>

namespace logging = boost::log;
namespace src = boost::log::sources;
namespace sinks = boost::log::sinks;
namespace keywords = boost::log::keywords;
namespace attrs = boost::log::attributes;
namespace expr = boost::log::expressions;

#define APP_NAME	"LOG_TEST"

enum class LogLevel: uint32_t
{
	trace = 0,
	debug,
	info,
	notice,
	warning,
	error,
	critical,
	fatal,
};

BOOST_LOG_ATTRIBUTE_KEYWORD(LogSeverity, "Severity", LogLevel)
BOOST_LOG_ATTRIBUTE_KEYWORD(LogTimeStamp, "TimeStamp", boost::posix_time::ptime)
BOOST_LOG_ATTRIBUTE_KEYWORD(LogScope, "Scope", attrs::named_scope::value_type)
BOOST_LOG_ATTRIBUTE_KEYWORD(LogThreadID, "ThreadID", attrs::current_thread_id::value_type)
BOOST_LOG_ATTRIBUTE_KEYWORD(LogProcessID, "ProcessID", attrs::current_process_id::value_type)
BOOST_LOG_ATTRIBUTE_KEYWORD(LogProcess, "Process", attrs::current_process_name::value_type)


template< typename CharT, typename TraitsT >
inline std::basic_ostream< CharT, TraitsT >& operator<< (
    std::basic_ostream< CharT, TraitsT >& strm, LogLevel lvl)
{
    static const char* const str[] =
    {
		"trace",
		"debug",
		"info",
		"notice",
		"warning",
		"error",
		"critical",
		"fatal",
    };
    if (static_cast< std::size_t >(lvl) < (sizeof(str) / sizeof(*str)))
        strm << str[static_cast< int >(lvl)];
    else
        strm << static_cast< int >(lvl);
    return strm;
}

class Log
{
public:
	enum class Handler: uint32_t
	{
		Console,
		File
	};
public:
	static Log* Instance()
	{
		static std::once_flag instanceFlag;
		std::call_once(instanceFlag, [&](){
			m_logService = new Log();
		});
		return m_logService;
	}

	// void SetLevel(LogLevel level);
	// void AddHandler(Handler handler);
	// void RemoveHandler(Handler handler);
	// void Format();

private:
	Log()
	{
		logging::add_common_attributes();
		logging::core::get()->add_thread_attribute("Scope", attrs::named_scope());
		logging::core::get()->add_global_attribute("ProcessID", attrs::current_process_id());
    	logging::core::get()->add_global_attribute("Process",attrs::current_process_name());

		logging::add_console_log(
			std::clog,
			keywords::format = expr::format("[%1%]<%2%>\t %3%")
									% expr::format_date_time(LogTimeStamp, "%Y-%m-%d %H:%M:%S.%f")
									% LogSeverity
									% expr::message
		);
		// auto fileName = boost::format("%1%(%2%)_%N.log")
		// 			% LogThreadID
		// 			% 2;
		
		std::cout << std::format("{}_%N.log", 1) << std::endl;
	
		// std::string fileName = std::string(LogProcess) + std::string(".") + std::string("%N.log");
		auto fileSink = logging::add_file_log(
			// keywords::file_name = APP_NAME"_%Y-%m-%d_%H-%M-%S.%ProcessID_%N.log",
			// keywords::file_name = fileName.c_str(),
			keywords::file_name = "test.log",
			// keywords::target_file_name = "TEST_%Y%m%d_%H%M%S_%N.log",
			// keywords::file_name = expr::attr<attrs::current_thread_id::value_type>("ThreadID"),
			keywords::rotation_size = 10*1024*1024,
			keywords::max_files = 10,
			keywords::format = expr::format("%1%(%2%) [%3%] <%4%> %5%")
									% expr::format_date_time(LogTimeStamp, "%Y-%m-%d %H:%M:%S.%f")
									% LogThreadID
									% expr::format_named_scope(LogScope, keywords::format = "(%F:%l)%n")
									% LogSeverity
									% expr::message
		);
	}
public:
	static src::severity_logger<LogLevel> 	logger;
private:
	static Log*								m_logService;
};

Log* Log::m_logService = nullptr;
src::severity_logger<LogLevel> Log::logger;

#define LOG(level)  	BOOST_LOG_FUNCTION();BOOST_LOG_SEV(Log::logger, level)

#define LOG_TRACE			LOG(LogLevel::trace)
#define LOG_DEBUG			LOG(LogLevel::debug)
#define LOG_INFO			LOG(LogLevel::info)
#define LOG_NOTICE			LOG(LogLevel::notice)
#define LOG_WARNING			LOG(LogLevel::warning)
#define LOG_ERROR			LOG(LogLevel::error)
#define LOG_CRITICAL		LOG(LogLevel::critical)
#define LOG_FATAL			LOG(LogLevel::fatal)


