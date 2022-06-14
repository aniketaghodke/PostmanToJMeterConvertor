import json
import re
import sys
import logging
import os

logging.basicConfig(level=logging.INFO)

########### Global Declarations #########

baseline_jmx = '<?xml version="1.0" encoding="UTF-8"?> <jmeterTestPlan version="1.2" properties="5.0" jmeter="5.2.1">   <hashTree>     <TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="JMeter Test Plan" enabled="true">       <stringProp name="TestPlan.comments"></stringProp>       <boolProp name="TestPlan.functional_mode">false</boolProp>       <boolProp name="TestPlan.serialize_threadgroups">false</boolProp>       <elementProp name="TestPlan.user_defined_variables" elementType="Arguments" guiclass="ArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">         <collectionProp name="Arguments.arguments"/>       </elementProp>       <stringProp name="TestPlan.user_define_classpath"></stringProp>     </TestPlan>     <hashTree>       <CacheManager guiclass="CacheManagerGui" testclass="CacheManager" testname="HTTP Cache Manager" enabled="true">         <boolProp name="clearEachIteration">true</boolProp>         <boolProp name="useExpires">true</boolProp>         <boolProp name="CacheManager.controlledByThread">false</boolProp>       </CacheManager>       <hashTree/>       <Arguments guiclass="ArgumentsPanel" testclass="Arguments" testname="User Defined Variables - EDIT ALL VARIABLES HERE!" enabled="true">         <collectionProp name="Arguments.arguments">           <elementProp name="THREADS" elementType="Argument">             <stringProp name="Argument.name">THREADS</stringProp>             <stringProp name="Argument.value">10</stringProp>             <stringProp name="Argument.metadata">=</stringProp>             <stringProp name="Argument.desc">Change as per requirement</stringProp>           </elementProp>           <elementProp name="THREADS_RAMPUP_TIME" elementType="Argument">             <stringProp name="Argument.name">THREADS_RAMPUP_TIME</stringProp>             <stringProp name="Argument.value">10</stringProp>             <stringProp name="Argument.desc">Value in seconds - Change as per requirement</stringProp>             <stringProp name="Argument.metadata">=</stringProp>           </elementProp>           <elementProp name="START_TPS" elementType="Argument">             <stringProp name="Argument.name">START_TPS</stringProp>             <stringProp name="Argument.value">5</stringProp>             <stringProp name="Argument.metadata">=</stringProp>             <stringProp name="Argument.desc">Change as per requirement</stringProp>           </elementProp>           <elementProp name="END_TPS" elementType="Argument">             <stringProp name="Argument.name">END_TPS</stringProp>             <stringProp name="Argument.value">5</stringProp>             <stringProp name="Argument.metadata">=</stringProp>             <stringProp name="Argument.desc">Change as per requirement</stringProp>           </elementProp>           <elementProp name="TEST_DURATION" elementType="Argument">             <stringProp name="Argument.name">TEST_DURATION</stringProp>             <stringProp name="Argument.value">60</stringProp>             <stringProp name="Argument.metadata">=</stringProp>             <stringProp name="Argument.desc">Value in seconds - Change as per requirement</stringProp>           </elementProp>         </collectionProp>         <stringProp name="TestPlan.comments">EDIT ALL VARIABLES HERE!</stringProp>       </Arguments>       <hashTree/>       <ResponseAssertion guiclass="AssertionGui" testclass="ResponseAssertion" testname="Global Response Assertion" enabled="true">         <collectionProp name="Asserion.test_strings">           <stringProp name="1538630">20\d</stringProp>         </collectionProp>         <stringProp name="Assertion.custom_message"></stringProp>         <stringProp name="Assertion.test_field">Assertion.response_code</stringProp>         <boolProp name="Assertion.assume_success">false</boolProp>         <intProp name="Assertion.test_type">2</intProp>       </ResponseAssertion>       <hashTree/>       <kg.apc.jmeter.timers.VariableThroughputTimer guiclass="kg.apc.jmeter.timers.VariableThroughputTimerGui" testclass="kg.apc.jmeter.timers.VariableThroughputTimer" testname="LOAD / SOAK TEST - Throughput Shaping Timer" enabled="true">         <collectionProp name="load_profile">           <collectionProp name="731866749">             <stringProp name="1606799354">${START_TPS}</stringProp>             <stringProp name="779619553">${END_TPS}</stringProp>             <stringProp name="-1857560941">${TEST_DURATION}</stringProp>           </collectionProp>         </collectionProp>       </kg.apc.jmeter.timers.VariableThroughputTimer>       <hashTree/>       <kg.apc.jmeter.timers.VariableThroughputTimer guiclass="kg.apc.jmeter.timers.VariableThroughputTimerGui" testclass="kg.apc.jmeter.timers.VariableThroughputTimer" testname="CAPACITY TEST - Throughput Shaping Timer" enabled="false">         <collectionProp name="load_profile">           <collectionProp name="1954571997">             <stringProp name="53">5</stringProp>             <stringProp name="53">5</stringProp>             <stringProp name="53430">600</stringProp>           </collectionProp>           <collectionProp name="1571222845">             <stringProp name="1567">10</stringProp>             <stringProp name="1567">10</stringProp>             <stringProp name="53430">600</stringProp>           </collectionProp>           <collectionProp name="1572182109">             <stringProp name="1572">15</stringProp>             <stringProp name="1572">15</stringProp>             <stringProp name="53430">600</stringProp>           </collectionProp>         </collectionProp>       </kg.apc.jmeter.timers.VariableThroughputTimer>       <hashTree/>       <ResultCollector guiclass="SummaryReport" testclass="ResultCollector" testname="Summary Report" enabled="true">         <boolProp name="ResultCollector.error_logging">false</boolProp>         <objProp>           <name>saveConfig</name>           <value class="SampleSaveConfiguration">             <time>true</time>             <latency>true</latency>             <timestamp>true</timestamp>             <success>true</success>             <label>true</label>             <code>true</code>             <message>true</message>             <threadName>true</threadName>             <dataType>true</dataType>             <encoding>false</encoding>             <assertions>true</assertions>             <subresults>true</subresults>             <responseData>false</responseData>             <samplerData>false</samplerData>             <xml>false</xml>             <fieldNames>true</fieldNames>             <responseHeaders>false</responseHeaders>             <requestHeaders>false</requestHeaders>             <responseDataOnError>false</responseDataOnError>             <saveAssertionResultsFailureMessage>true</saveAssertionResultsFailureMessage>             <assertionsResultsToSave>0</assertionsResultsToSave>             <bytes>true</bytes>             <sentBytes>true</sentBytes>             <threadCounts>true</threadCounts>             <idleTime>true</idleTime>             <connectTime>true</connectTime>           </value>         </objProp>         <stringProp name="filename"></stringProp>       </ResultCollector>       <hashTree/>       <ResultCollector guiclass="ViewResultsFullVisualizer" testclass="ResultCollector" testname="View Results Tree" enabled="true">         <boolProp name="ResultCollector.error_logging">false</boolProp>         <objProp>           <name>saveConfig</name>           <value class="SampleSaveConfiguration">             <time>true</time>             <latency>true</latency>             <timestamp>true</timestamp>             <success>true</success>             <label>true</label>             <code>true</code>             <message>true</message>             <threadName>true</threadName>             <dataType>false</dataType>             <encoding>false</encoding>             <assertions>true</assertions>             <subresults>false</subresults>             <responseData>false</responseData>             <samplerData>false</samplerData>             <xml>false</xml>             <fieldNames>true</fieldNames>             <responseHeaders>false</responseHeaders>             <requestHeaders>false</requestHeaders>             <responseDataOnError>true</responseDataOnError>             <saveAssertionResultsFailureMessage>true</saveAssertionResultsFailureMessage>             <assertionsResultsToSave>0</assertionsResultsToSave>             <bytes>true</bytes>             <hostname>true</hostname>             <threadCounts>true</threadCounts>             <sampleCount>true</sampleCount>           </value>         </objProp>         <stringProp name="filename"></stringProp>       </ResultCollector>       <hashTree/>       <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="Thread Group" enabled="true">         <stringProp name="ThreadGroup.on_sample_error">startnextloop</stringProp>         <elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller" enabled="true">           <boolProp name="LoopController.continue_forever">false</boolProp>           <intProp name="LoopController.loops">-1</intProp>         </elementProp>         <stringProp name="ThreadGroup.num_threads">${THREADS}</stringProp>         <stringProp name="ThreadGroup.ramp_time">${THREADS_RAMPUP_TIME}</stringProp>         <boolProp name="ThreadGroup.scheduler">false</boolProp>         <stringProp name="ThreadGroup.duration"></stringProp>         <stringProp name="ThreadGroup.delay"></stringProp>         <boolProp name="ThreadGroup.same_user_on_next_iteration">false</boolProp>       </ThreadGroup>       <hashTree/>     </hashTree>   </hashTree> </jmeterTestPlan>'
TG_TC_HTTPSampler_jmx = '        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="Request_MY-NAME" enabled="true">DYNAMIC-BODY-PART<stringProp name="HTTPSampler.domain"></stringProp>           <stringProp name="HTTPSampler.port"></stringProp>           <stringProp name="HTTPSampler.protocol"></stringProp>           <stringProp name="HTTPSampler.contentEncoding"></stringProp>           <stringProp name="HTTPSampler.path">MY-PATH</stringProp>           <stringProp name="HTTPSampler.method">MY-METHOD</stringProp>           <boolProp name="HTTPSampler.follow_redirects">true</boolProp>           <boolProp name="HTTPSampler.auto_redirects">false</boolProp>           <boolProp name="HTTPSampler.use_keepalive">true</boolProp>           <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>           <stringProp name="HTTPSampler.embedded_url_re"></stringProp>           <stringProp name="HTTPSampler.connect_timeout"></stringProp>           <stringProp name="HTTPSampler.response_timeout"></stringProp>         </HTTPSamplerProxy>'
headerStringStart_jmx = '          <hashTree>             <HeaderManager guiclass="HeaderPanel" testclass="HeaderManager" testname="HTTP Header Manager" enabled="true">               <collectionProp name="HeaderManager.headers">'
headerStringEnd_jmx = '              </collectionProp>             </HeaderManager>             <hashTree/>           </hashTree>'

raw_body_part = '          <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>           <elementProp name="HTTPsampler.Arguments" elementType="Arguments">             <collectionProp name="Arguments.arguments">               <elementProp name="" elementType="HTTPArgument">                 <boolProp name="HTTPArgument.always_encode">false</boolProp>                 <stringProp name="Argument.value">MY-BODY</stringProp>                 <stringProp name="Argument.metadata">=</stringProp>               </elementProp>             </collectionProp>           </elementProp>'
without_body_part = '          <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">             <collectionProp name="Arguments.arguments"/>           </elementProp>'

itr_jmx = ''
itr_final_jmx = ''

########### Code  #########

inputpath = input("Enter full directory path where Postman collection is parked along with environment variables and/or global variables, if defined: ")

try:
    for i in os.listdir(inputpath):
         if "collection" in i:
            outfileName = i.split('.')[0]
            inputfile = inputpath+"/"+i
         if "environment" in i:
            variablefile = inputpath+"/"+i
         if "globals" in i:
            globalvariablefile = inputpath+"/"+i

    with open(inputfile, 'r') as rf:
        fileContent = rf.read()
        jsonFile = json.loads(fileContent)  # jsonFile type dict
        level_1 = jsonFile['item']  # level_1 type list

except Exception as e:
    logging.error('Something went wrong while opening input files' + str(e))
    sys.exit(1)

dirname = os.path.dirname(inputfile)
outfile = dirname+'/'+outfileName+'.jmx'

num = 0
for i in level_1: # i type dict

    if 'item' in i:
        logging.error('A collection containing folders is not handled, kindly add requests directly under collection without any folders and retry.')
        sys.exit(1)

    num = num + 1
    temp_jmx = ''
    headerStringMid_jmx = ''
    paramStringMid = ''

    #Name
    # print(i['name'])
    myName = i['name']
    myNameUpdated = str(num) + '_' + myName
    temp_jmx = TG_TC_HTTPSampler_jmx.replace('MY-NAME', myNameUpdated)

    #method
    # print(i['request']['method'])
    myMethod = i['request']['method']
    temp_jmx = temp_jmx.replace('MY-METHOD', myMethod)

    #url
    # print(i['request']['url']['raw'])
    myURL = i['request']['url']['raw']
    myURL = re.sub('&', '&amp;', myURL)
    temp_jmx = temp_jmx.replace('MY-PATH', myURL)

    # Body
    try:
        myRequestBodyType = i['request']['body']['mode']

        if myRequestBodyType == 'raw':
            myRequestBody = i['request']['body']['raw']
            myRequestBody = myRequestBody.replace('\n','')

            # Following transformations for xml body.
            myRequestBody = re.sub(r'&', '&amp;', myRequestBody)
            myRequestBody = re.sub('<', '&lt;', myRequestBody)
            myRequestBody = re.sub('>', '&gt;', myRequestBody)
            myRequestBody = re.sub(r'\\"', '&quot;', myRequestBody)
            myRequestBody = myRequestBody.replace("\\r\\n", "\n")

            body_part = raw_body_part.replace('MY-BODY', myRequestBody)
            temp_jmx = temp_jmx.replace('DYNAMIC-BODY-PART', body_part)

        if (myRequestBodyType == 'urlencoded'):
            myRequestBody = i['request']['body']['urlencoded']

        if (myRequestBodyType == 'formdata'):
            myRequestBody = i['request']['body']['formdata']

            for j in myRequestBody:
                if ('disabled' in j) and (j['disabled'] == True):
                    pass
                else:
                    param_to_add = '<elementProp name="'+j['key']+'" elementType="HTTPArgument"> <boolProp name="HTTPArgument.always_encode">true</boolProp> <stringProp name="Argument.value">'+j['value']+'</stringProp> <stringProp name="Argument.metadata">=</stringProp> <boolProp name="HTTPArgument.use_equals">true</boolProp> <stringProp name="Argument.name">'+j['key']+'</stringProp> </elementProp>'
                    paramStringMid = paramStringMid + param_to_add

            paramString_All = '<collectionProp name="Arguments.arguments">'+paramStringMid+'</collectionProp></elementProp>'
            paramString_ToAdd = without_body_part.replace('<collectionProp name="Arguments.arguments"/>           </elementProp>',paramString_All)
            temp_jmx = temp_jmx.replace('DYNAMIC-BODY-PART',paramString_ToAdd)
    except:
        checkForQuery = i['request']['url']
        if 'query' in checkForQuery:
            for q in checkForQuery['query']:
                if ('disabled' in q) and (q['disabled'] == True):
                    pass
                else:
                    param_to_add = '<elementProp name="'+q['key']+'" elementType="HTTPArgument"> <boolProp name="HTTPArgument.always_encode">true</boolProp> <stringProp name="Argument.value">'+q['value']+'</stringProp> <stringProp name="Argument.metadata">=</stringProp> <boolProp name="HTTPArgument.use_equals">true</boolProp> <stringProp name="Argument.name">'+q['key']+'</stringProp> </elementProp>'
                    paramStringMid = paramStringMid + param_to_add

            paramString_All = '<collectionProp name="Arguments.arguments">' + paramStringMid + '</collectionProp></elementProp>'
            paramString_ToAdd = without_body_part.replace('<collectionProp name="Arguments.arguments"/>           </elementProp>', paramString_All)
            temp_jmx = temp_jmx.replace('DYNAMIC-BODY-PART', paramString_ToAdd)
        else:
            temp_jmx = temp_jmx.replace('DYNAMIC-BODY-PART', without_body_part)

    # Headers
    try:
        myHeaders = i['request']['header']
        for k in myHeaders:
            if ('disabled' in k) and (k['disabled'] == True):
                pass
            else:
                headerToAdd_jmx = '                <elementProp name="" elementType="Header">                   <stringProp name="Header.name">' + k['key'] + '</stringProp>                   <stringProp name="Header.value">' + k['value'] + '</stringProp>                 </elementProp>'
                headerStringMid_jmx = headerStringMid_jmx + headerToAdd_jmx
        header_JMX = headerStringStart_jmx + headerStringMid_jmx + headerStringEnd_jmx
        itr_jmx = temp_jmx + header_JMX
        itr_final_jmx = itr_final_jmx + itr_jmx
    except:
        pass
        # A blank HTTP Header manager will get added if there are no headers or all disabled headers.
        # except block will not get called as even in case of no headers or all disabled headers '[]' will be there."header": [],

baseline_jmx_find = '</ThreadGroup>       <hashTree/>     </hashTree>   </hashTree> </jmeterTestPlan>'
baseline_jmx_replace = '</ThreadGroup>'+ '<hashTree>'+ itr_final_jmx + '</hashTree>'+ '</hashTree>   </hashTree> </jmeterTestPlan>'
output = baseline_jmx.replace(baseline_jmx_find,baseline_jmx_replace)
# print(output)

# processing variables file if provided
try:
    with open(variablefile, 'r') as rf:
        variablefileContent = rf.read()
        jsonFile = json.loads(variablefileContent)  # jsonFile type dict
        level_1 = jsonFile['values']  # level_1 type list

        current_UDV = re.search(r'<collectionProp name="Arguments.arguments">(.*?)</collectionProp>', output)
        imported_UDV = ''

        for i in level_1:
            myStr = '<elementProp name="'+i['key']+'" elementType="Argument">            <stringProp name="Argument.name">'+i['key']+'</stringProp>            <stringProp name="Argument.value">'+i['value']+'</stringProp>            <stringProp name="Argument.metadata">=</stringProp>            <stringProp name="Argument.desc">Imported from environment variables </stringProp>          </elementProp>'
            imported_UDV = imported_UDV + myStr

            to_find = '{{'+i['key']+'}}'
            to_replace = '${'+i['key']+'}'
            output = output.replace(to_find,to_replace)

        final_UDV = current_UDV.group(1) + imported_UDV
        output = output.replace(current_UDV.group(1),final_UDV)
except Exception as e:
    logging.info('Either "ENVIRONMENT VARIABLES" file not provided or something went wrong while opening it! ' + str(e))


# processing global variables file if provided
try:
    with open(globalvariablefile, 'r') as rf:
        globalvariablefileContent = rf.read()
        jsonFile = json.loads(globalvariablefileContent)  # jsonFile type dict
        level_1 = jsonFile['values']  # level_1 type list

        current_UDV = re.search(r'<collectionProp name="Arguments.arguments">(.*?)</collectionProp>', output)
        imported_UDV = ''

        for i in level_1:
            myStr = '<elementProp name="'+i['key']+'" elementType="Argument">            <stringProp name="Argument.name">'+i['key']+'</stringProp>            <stringProp name="Argument.value">'+i['value']+'</stringProp>            <stringProp name="Argument.metadata">=</stringProp>            <stringProp name="Argument.desc">Imported from global variables </stringProp>          </elementProp>'
            imported_UDV = imported_UDV + myStr

            to_find = '{{'+i['key']+'}}'
            to_replace = '${'+i['key']+'}'
            output = output.replace(to_find,to_replace)

        final_UDV = current_UDV.group(1) + imported_UDV
        output = output.replace(current_UDV.group(1),final_UDV)
except Exception as e:
    logging.info('Either "GLOBAL VARIABLES" file not provided or something went wrong while opening it! ' + str(e))


# Writing final 'output' to outfile
try:
    with open (outfile,'w+') as wf:
        wf.write(output)
        logging.info('Successfully created jmeter JMX file & Parked at location: ' +outfile)
except Exception as e:
    logging.error('Something went wrong while opening "OUTPUT" file' + str(e))
    sys.exit()