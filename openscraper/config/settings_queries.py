# -*- encoding: utf-8 -*-

from settings_corefields import DATAMODEL_FIELDS_TYPES


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### QUERIES ARGS - API #####################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

QUERIES_ARGS_TO_IGNORE_IF_API = [
	# "page_n",
	"open_level"
]
QUERIES_ARGS_ACCEPTED_AS_FIRST_QUERY_TERMS = [
	"spider_id",
	"search_for",
	# "search_in",
	"open_level"
]
QUERIES_MAX_RESULTS_IF_API = 100


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### QUERIES ARGS - INFOS #####################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### DATA QUERIES FROM URL - reconstruct from slug
QUERY_INFOS_BY_DEFAULT = {
	"only_dm_list"		: False,		# retrieve only dm_set list 
	"only_spiders_list"	: False,		# retrieve only spiders list 
	"get_all_spiders"	: False,		# retrieve only spiders list 
}
# # adding search_in_* by field type if present in slug == authorized DATAMODEL_FIELDS_TYPES
# QUERY_INFOS_BY_TYPE = {
# 	"search_in_" + field_type : None for field_type in DATAMODEL_FIELDS_TYPES
# }
# QUERY_INFOS_BY_TYPE_REVERSE = {
# 	"search_in_" + field_type : field_type for field_type in DATAMODEL_FIELDS_TYPES
# }
# QUERY_INFOS_BY_DEFAULT.update(QUERY_DATA_BY_TYPE)


QUERIES_INFOS_ALLOWED_UNIQUE = [
	"only_dm_list",
	"only_spiders_list",
	"get_all_spiders",
]
QUERIES_INFOS_ALLOWED_INTEGERS  	= [
	
]
QUERIES_INFOS_ALLOWED_POSITIVES 	= [
	
]
QUERIES_INFOS_ALLOWED_BOOLEAN = [
	"only_dm_list", 
	"only_spiders_list",
	"get_all_spiders",
]

### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### QUERIES ARGS - STATS #####################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### DATA QUERIES FROM URL - reconstruct from slug
QUERY_STATS_BY_DEFAULT = {
	"only_counts_simple"	: False,		# retrieve only 
	"only_tags_stats"		: False,		# retrieve only 
	"only_spiders_stats"	: False,		# retrieve only 
}
# # adding search_in_* by field type if present in slug == authorized DATAMODEL_FIELDS_TYPES
# QUERY_INFOS_BY_TYPE = {
# 	"search_in_" + field_type : None for field_type in DATAMODEL_FIELDS_TYPES
# }
# QUERY_INFOS_BY_TYPE_REVERSE = {
# 	"search_in_" + field_type : field_type for field_type in DATAMODEL_FIELDS_TYPES
# }
# QUERY_INFOS_BY_DEFAULT.update(QUERY_DATA_BY_TYPE)


QUERIES_STATS_ALLOWED_UNIQUE = [
	"only_counts_simple",
	"only_tags_stats",
	"only_spiders_stats",
]
QUERIES_STATS_ALLOWED_INTEGERS  	= [
	
]
QUERIES_STATS_ALLOWED_POSITIVES 	= [
	
]
QUERIES_STATS_ALLOWED_BOOLEAN = [
	"only_counts_simple",
	"only_tags_stats",
	"only_spiders_stats",
]



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### QUERIES ARGS - DATA #####################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### DATA QUERIES FROM URL - reconstruct from slug
QUERY_DATA_BY_DEFAULT = {
	"page_n"			: 1,			# page number
	"results_per_page" 	: 25,			# self-explanatory
	"token"				: None, 		# TO DO LATER : client's JWT (token) to check permissions 
	"spider_id"			: ["all"], 		# spider_id for contributor(s)
	"item_id"			: None, 		# item_id for item(s)
	"is_complete"		: False, 		# only complete records... a bit optimistic isn't it ?
	"search_for"		: [],			# list of words to search in data collection
	# "search_in"		: [],			# list of fields to search in
	# "filter_by_types"	: {},
	"open_level"		: "opendata",	# fields of data to be shown -> "all" == "opendata" + "commons" + "private"
	"all_results"		: False,		# to override results_per_page <-- only to be required by solidata instance sharing same secret key
	"added_by"			: None,			# list of user having added the data 
	"sort_by"			: None,
	"shuffle_seed"		: None,			# seed to randomize list order
	# "only_dm_list"		: False,		# retrieve only dm_set list 
	# "only_spiders_list"	: False,		# retrieve only spiders list 
	"export_as_csv"		: False,		# export as csv
}
# adding search_in_* by field type if present in slug == authorized DATAMODEL_FIELDS_TYPES
QUERY_DATA_BY_TYPE = {
	"search_in_" + field_type : None for field_type in DATAMODEL_FIELDS_TYPES
}
QUERY_DATA_BY_TYPE_REVERSE = {
	"search_in_" + field_type : field_type for field_type in DATAMODEL_FIELDS_TYPES
}
QUERY_DATA_BY_DEFAULT.update(QUERY_DATA_BY_TYPE)


QUERIES_DATA_ALLOWED_UNIQUE = [
	"page_n", 
	"results_per_page", 
	"token", 
	"item_id", 
	"is_complete", 
	"open_level",
	"all_results",
	"sort_by",
	"shuffle_seed",
	# "only_dm_list",
	# "only_spiders_list",
	"export_as_csv",
]
QUERIES_DATA_ALLOWED_INTEGERS  	= [
	"page_n", "results_per_page", "shuffle_seed"
]
QUERIES_DATA_ALLOWED_POSITIVES 	= [
	"page_n", "results_per_page", "shuffle_seed"
]
QUERIES_DATA_ALLOWED_BOOLEAN = [
	"is_complete", "all_results", 
	# "only_dm_list", 
	# "only_spiders_list", 
	"export_as_csv"
]


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### QUERIES ARGS - SPIDERS ##################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### SPIDER QUERIES FROM URL - reconstruct from slug
QUERY_SPIDER_BY_DEFAULT = {
	"page_n"			: 1,		# page number
	"results_per_page" 	: 10,		# self-explanatory
	"token"				: None, 	# TO DO LATER : client's JWT (token) to check permissions 
	"spider_id"			: ["all"], 	# spider_id for contributor(s)
	"is_working"		: "any",	# 
	"all_results"		: False,		# to overide results_per_page
	"sort_by"			: None,
	"shuffle_seed"		: None,
}
QUERIES_SPIDER_ALLOWED_UNIQUE = [
	"page_n", 
	"results_per_page",
	"token", 
	"is_working", 
	"all_results",
	"sort_by"

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
QUERY_RESET  = "reset_data"
QUERY_DELETE = "is_delete"



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### QUERIES ARGS - CRAWLING ##################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### SPIDER CRAWLER QUERIES FROM URL - basic args in slug query for crawling
QUERY_CRAWL_BY_DEFAULT = {
	"token"			: None, 	# TO DO LATER : client's JWT (token) to check permissions 
	"spider_id" 	: None,
	# "test"			: False,
	"test_limit" 	: None,
	"next"			: None
}
QUERIES_CRAWL_ALLOWED_UNIQUE = {
	"spider_id",
	"test",
	"test_limit",
	"token", 
	"next",
}
QUERIES_CRAWL_ALLOWED_INTEGERS = {
	"test_limit",
	"next",
}
QUERIES_CRAWL_ALLOWED_POSITIVES = {
	"test_limit",
}
QUERIES_CRAWL_ALLOWED_BOOLEAN = {
	"test",
}