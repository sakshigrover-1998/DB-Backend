from django.shortcuts import render
from django.core.cache import caches
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
from .models import FlagInsertTable
from django.forms.models import model_to_dict

def onDataInsert(isExceptionData):
    # make it true
    print("The cache needs to be updated")

    obj = FlagInsertTable.objects.get(isException = isExceptionData)
    
    obj.Flag = True
    
    obj.save()

def onCacheUpdate(isExceptionData):

    # make it false
    print("The cache is now updated")
    obj = FlagInsertTable.objects.get(isException = isExceptionData)

    obj.Flag = False
    obj.save()
import FastData.views as FastDataViews
from Exceptions.models import ExceptionType
from django.http import HttpResponse
from datetime import date
@api_view(['GET',])
def getCacheContent(request, userBL, userRegion):
    onDataInsert(True)
    from time import time
    start = time()  
    
    # rows = ExceptionType.objects.filter(exception_COBDT = date.today())
    # print("Time taken to run the query:", time() - start," seconds")

    print("Cache",cache.get("finalDict"))

    if(cache.get('finalDict') == None):
        print("Cache is empty")
        finalDict = {

        }
        checkDict = {

        }
        FastDataViews.onDataInsert(isExceptionData=True)
        
    else:

        finalDict = cache.get("finalDict")
        checkDict = cache.get("checkDict")


    if(FlagInsertTable.objects.all()[0].Flag == True):
        # Update cache
        print("The cache needs to be updated")
        # get data from the model for current cobdt and insert into cache
        # finalDict = [ x.exception_ID for x in ExceptionType.objects.filter(exception_COBDT = date.today()) ]#the data
        rows = ExceptionType.objects.filter(exception_COBDT = date.today())
        # rows = ExceptionType.objects.all()


        
        for i in rows:
            exception_BusinessLine = i.exception_BusinessLine
            exception_Region = i.exception_Region
            row_ID = i.id
            if(exception_BusinessLine not in checkDict):
                print(exception_BusinessLine,"not in cache")
                checkDict[exception_BusinessLine] = {}
                checkDict[exception_BusinessLine][exception_Region] = set()
                finalDict[exception_BusinessLine] = {}
                finalDict[exception_BusinessLine][exception_Region] = []
            elif(exception_Region not in checkDict[exception_BusinessLine]):
                print(exception_Region, "not in cache")

                checkDict[exception_BusinessLine][exception_Region] = set()
                finalDict[exception_BusinessLine][exception_Region] = []
            else:
                print(exception_BusinessLine, exception_Region, "in cache")
            if(row_ID not in checkDict[exception_BusinessLine][exception_Region]):
                finalDict[exception_BusinessLine][exception_Region].append(model_to_dict(i))
                checkDict[exception_BusinessLine][exception_Region].add(row_ID)

        cache.set("finalDict", finalDict, 24*60*60) 
        cache.set("checkDict", checkDict, 24*60*60)
        # TODO QUERY THE MODEL
        FastDataViews.onCacheUpdate(isExceptionData=True)
    else:
        print("The cache is up to date")
    print("Cache",cache.get("finalDict"))
    # cache has all the data
    # check if business line and region in cache in cache and return
    print("Time taken to run:", time() - start," seconds")
    if(userBL == "ALL"):
        # return the whole caache
        print("THE WHOLE CACHE")
        print(finalDict)
        rowList = []
        for bline in finalDict.keys():
            for bregion in finalDict[bline]:
                rowList.extend(finalDict[bline][bregion])
        return Response(rowList)
        
    if(userBL  in checkDict):
        if(userRegion in checkDict[userBL]):
            return Response(finalDict[userBL][userRegion])
    return Response([])



from Filters.models import FilterData

@api_view(['GET',])
def getFilterCacheContent(request, userBL, userRegion):
    from time import time
    start = time()  
    print("Cache",cache.get("filterfinalDict"))

    if(cache.get('filterfinalDict') == None):
        print("Cache is empty")
        filterfinalDict = {

        }
        filtercheckDict = {

        }
        FastDataViews.onDataInsert(False)
        
    else:

        filterfinalDict = cache.get("filterfinalDict")
        filtercheckDict = cache.get("filtercheckDict")


    if(FlagInsertTable.objects.all()[1].Flag == True):
        # Update cache
        print("The filter cache needs to be updated")
        # get data from the model for current cobdt and insert into cache
        # filterfinalDict = [ x.exception_ID for x in ExceptionType.objects.filter(exception_COBDT = date.today()) ]#the data
        rows = FilterData.objects.filter(cob_dt = date.today())
        for i in rows:
            exception_BusinessLine = i.business_line
            exception_Region = i.region
            row_ID = i.id
            if(exception_BusinessLine not in filtercheckDict):
                print(exception_BusinessLine,"not in cache")
                filtercheckDict[exception_BusinessLine] = {}
                filtercheckDict[exception_BusinessLine][exception_Region] = set()
                filterfinalDict[exception_BusinessLine] = {}
                filterfinalDict[exception_BusinessLine][exception_Region] = []
            elif(exception_Region not in filtercheckDict[exception_BusinessLine]):
                print(exception_Region, "not infilter cache")

                filtercheckDict[exception_BusinessLine][exception_Region] = set()
                filterfinalDict[exception_BusinessLine][exception_Region] = []
            else:
                print(exception_BusinessLine, exception_Region, "in cache")
            if(row_ID not in filtercheckDict[exception_BusinessLine][exception_Region]):
                filterfinalDict[exception_BusinessLine][exception_Region].append(model_to_dict(i))
                filtercheckDict[exception_BusinessLine][exception_Region].add(row_ID)

        cache.set("filterfinalDict", filterfinalDict, 24*60*60) 
        cache.set("filtercheckDict", filtercheckDict, 24*60*60)
        # TODO QUERY THE MODEL
        FastDataViews.onCacheUpdate(False)
    else:
        print("The filter cache is up to date")
    print("Cache",cache.get("filterfinalDict"))
    # cache has all the data
    # check if business line and region in cache in cache and return
    print("Time taken to run:", time() - start," seconds")
    if(userBL == "ALL"):
        # return the whole caache
        print("THE WHOLE CACHE")
        rowList = []
        for bline in filterfinalDict.keys():
            for bregion in filterfinalDict[bline]:
                rowList.extend(filterfinalDict[bline][bregion])
        return Response(rowList)
    if(userBL  in filtercheckDict):
        if(userRegion in filtercheckDict[userBL]):
            return Response(filterfinalDict[userBL][userRegion])
    return Response([])
# def intermediate_loadFunction( data_dict):
#     return data_dict
    # print(data_dict)
    #   # format for this filterfinalDict will be
    #     # {

    #     #     region1:
    #     #     {
    #     #         bLine1: [ data for bLine1 ]
    #     #         bLine2: [data for bLine1]

    #     #     }
    #     #     region2:
    #     #     {
    #     #         bLine1: [ data for bLine1 ]
    #     #         bLine2: [data for bLine1]

    #     #     }
    #     # }
    #     # Another dict for checking if items already exist in the cache]
    #      # format for this filtercheckDict will be
    #     # {

    #     #     region1:
    #     #     {
    #     #         bLine1: set(exceptionID)
    #     #         bLine2: set(exceptionID)

    #     #     }
    #     #     region2:
    #     #     {
    #     #      bLine1: set(exceptionID)
    #     #         bLine2: set(exceptionID)

    #     #     }
    #     # }
    # if(cache.get('check_dict') == None):
    #     print("Cache is empty")
    #     finalDict = {

    #     }
    #     checkDict = {
            
    #     }
    # else:

    #     finalDict = cache.get("data_dict")
    #     checkDict = cache.get("check_dict")
    #     print("Previous data of dict", finalDict)
 
    #     exception_BusinessLine = data_dict['exception_BusinessLine']
    #     exception_Region = data_dict['exception_Region']
    #     row_ID = data_dict['id']

        # if(exception_BusinessLine not in checkDict):
        #     print(exception_BusinessLine,"not in cache")
        #     checkDict[exception_BusinessLine] = {}
        #     checkDict[exception_BusinessLine][exception_Region] = set()
        #     finalDict[exception_BusinessLine] = {}
        #     finalDict[exception_BusinessLine][exception_Region] = []
        # elif(exception_Region not in checkDict[exception_BusinessLine]):
        #     print(exception_Region, "not in cache")

        #     checkDict[exception_BusinessLine][exception_Region] = set()
        #     finalDict[exception_BusinessLine][exception_Region] = []
        # else:
        #     print(exception_BusinessLine, exception_Region, "in cache")
    #     print("Appending into finaldict,", finalDict)
    #     if(row_ID not in checkDict[exception_BusinessLine][exception_Region]):
    #         finalDict[exception_BusinessLine][exception_Region].append(data_dict)
    #         print("checkDict is", checkDict)
    #         checkDict[exception_BusinessLine][exception_Region].add(row_ID)

    #         print("Appended into finaldict,", finalDict)
    #     else:
    #         print(id,"already in the cache")
            
    # cache.set("data_dict",finalDict)
    # cache.set("check_dict",checkDict)
    
    # print("Final content of cache:")
    # print(cache.get("check_dict"))
    # print("Cache content")
    # print(cache.get("data_dict"))



# @api_view(['GET',])
# def getCacheContent(request, businessLine, region):
#     print()
#     print(cache.get('data_dict'), caches["check_dict"])
#     if(cache.get('data_dict') == None):
#         print("no data in cache")
#         return Response([])
#     finalDict = cache.get("data_dict")

#     if(businessLine not in finalDict):

#         print(businessLine,"not in cache")
#         finalDict[businessLine] = {}
#         finalDict[businessLine][region] = []
#         return Response([]) 

#     elif(region not in finalDict[businessLine]):
#         print(region, "not in cache")

#         finalDict[businessLine][region] = set()
#         finalDict[businessLine][region] = []
#         return Response([]) 

#     else:
#         print(businessLine, region, "in cache")
        
#         return Response(finalDict[businessLine][region]) 
