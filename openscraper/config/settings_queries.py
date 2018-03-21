# -*- encoding: utf-8 -*-

DEFAULT_ERROR_ARGS_TO_DELETE = [
	"error", 
	"_xsrf"
]


### DATA QUERIES FROM URL - reconstruct from slug
QUERY_DATA_BY_DEFAULT = {
	"page_n"			: 1,		# page number
	"results_per_page" 	: 25,		# self-explanatory
	"token"				: None, 	# TO DO LATER : client's JWT (token) to check permissions 
	"spider_id"			: ["all"], 	# spider_id for contributor(s)
	"is_complete"		: False, 	# only complete records
	"search_for"		: [],		# list of words to search in data collection
	"search_in"			: [],		# list of fields to search in
	"open_level"		: ["all"],	# fields of data to be shown -> "all" == "opendata" + "commons" + "private"
	"all_results"		: False		# to overide results_per_page
}
QUERIES_DATA_ALLOWED_UNIQUE = [
	"page_n", 
	"results_per_page", 
	"token", 
	"is_complete", 
	"open_level",
	"all_results"
]
QUERIES_DATA_ALLOWED_INTEGERS  	= [
	"page_n", "results_per_page"
]
QUERIES_DATA_ALLOWED_POSITIVES 	= [
	"page_n", "results_per_page"
]
QUERIES_DATA_ALLOWED_BOOLEAN = [
	"is_complete", "all_results"
]




### SPIDER QUERIES FROM URL - reconstruct from slug
QUERY_SPIDER_BY_DEFAULT = {
	"page_n"			: 1,		# page number
	"results_per_page" 	: 25,		# self-explanatory
	"token"				: None, 	# TO DO LATER : client's JWT (token) to check permissions 
	"spider_id"			: ["all"], 	# spider_id for contributor(s)
	"is_working"		: "any",	# 
	"all_results"		: False		# to overide results_per_page
}
QUERIES_SPIDER_ALLOWED_UNIQUE = [
	"page_n", 
	"results_per_page",
	"token", 
	"is_working", 
	"all_results"
]
QUERIES_SPIDER_ALLOWED_INTEGERS  	= [
	"page_n", "results_per_page"
]
QUERIES_SPIDER_ALLOWED_POSITIVES  	= [
	"page_n", "results_per_page"
]
QUERIES_SPIDER_ALLOWED_BOOLEAN = [
	"all_results",
]





### SPIDER CRAWLER QUERIES FROM URL - basic args in slug query for crawling
QUERY_CRAWL_BY_DEFAULT = {
	"spider_id" 	: None,
	"test"			: True,
	"test_limit" 	: 1,
}
QUERIES_CRAWL_ALLOWED_UNIQUE = {
	"spider_id",
	"test",
	"test_limit",
}
QUERIES_CRAWL_ALLOWED_INTEGERS = {
	"test_limit",
}
QUERIES_CRAWL_ALLOWED_POSITIVES = {
	"test_limit",
}
QUERIES_CRAWL_ALLOWED_BOOLEAN = {
	"test",
}