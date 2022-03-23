########### Imports #########

import re
import sys
import logging
import os


logging.basicConfig(level=logging.INFO)

########### Global Declarations #########

# baseline_jmx = '<?xml version="1.0" encoding="UTF-8"?> <jmeterTestPlan version="1.2" properties="5.0" jmeter="5.2.1">   <hashTree>     <TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="JMeter Test Plan" enabled="true">       <stringProp name="TestPlan.comments"></stringProp>       <boolProp name="TestPlan.functional_mode">false</boolProp>       <boolProp name="TestPlan.serialize_threadgroups">false</boolProp>       <elementProp name="TestPlan.user_defined_variables" elementType="Arguments" guiclass="ArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">         <collectionProp name="Arguments.arguments"/>       </elementProp>       <stringProp name="TestPlan.user_define_classpath"></stringProp>     </TestPlan>     <hashTree>       <CacheManager guiclass="CacheManagerGui" testclass="CacheManager" testname="HTTP Cache Manager" enabled="true">         <boolProp name="clearEachIteration">true</boolProp>         <boolProp name="useExpires">true</boolProp>         <boolProp name="CacheManager.controlledByThread">false</boolProp>       </CacheManager>       <hashTree/>       <ResponseAssertion guiclass="AssertionGui" testclass="ResponseAssertion" testname="Global Response Assertion" enabled="true">         <collectionProp name="Asserion.test_strings">           <stringProp name="1538630">20\d</stringProp>         </collectionProp>         <stringProp name="Assertion.custom_message"></stringProp>         <stringProp name="Assertion.test_field">Assertion.response_code</stringProp>         <boolProp name="Assertion.assume_success">false</boolProp>         <intProp name="Assertion.test_type">2</intProp>       </ResponseAssertion>       <hashTree/>       <kg.apc.jmeter.timers.VariableThroughputTimer guiclass="kg.apc.jmeter.timers.VariableThroughputTimerGui" testclass="kg.apc.jmeter.timers.VariableThroughputTimer" testname="jp@gc - Throughput Shaping Timer" enabled="true">         <collectionProp name="load_profile">           <collectionProp name="-1917578236">             <stringProp name="-1302264996">${__P(TPS)}</stringProp>             <stringProp name="-1302264996">${__P(TPS)}</stringProp>             <stringProp name="-1489184538">${__P(TEST_DURATION)}</stringProp>           </collectionProp>         </collectionProp>       </kg.apc.jmeter.timers.VariableThroughputTimer>       <hashTree/>       <ResultCollector guiclass="SummaryReport" testclass="ResultCollector" testname="Summary Report" enabled="true">         <boolProp name="ResultCollector.error_logging">false</boolProp>         <objProp>           <name>saveConfig</name>           <value class="SampleSaveConfiguration">             <time>true</time>             <latency>true</latency>             <timestamp>true</timestamp>             <success>true</success>             <label>true</label>             <code>true</code>             <message>true</message>             <threadName>true</threadName>             <dataType>true</dataType>             <encoding>false</encoding>             <assertions>true</assertions>             <subresults>true</subresults>             <responseData>false</responseData>             <samplerData>false</samplerData>             <xml>false</xml>             <fieldNames>true</fieldNames>             <responseHeaders>false</responseHeaders>             <requestHeaders>false</requestHeaders>             <responseDataOnError>false</responseDataOnError>             <saveAssertionResultsFailureMessage>true</saveAssertionResultsFailureMessage>             <assertionsResultsToSave>0</assertionsResultsToSave>             <bytes>true</bytes>             <sentBytes>true</sentBytes>             <threadCounts>true</threadCounts>             <idleTime>true</idleTime>             <connectTime>true</connectTime>           </value>         </objProp>         <stringProp name="filename"></stringProp>       </ResultCollector>       <hashTree/>       <ResultCollector guiclass="ViewResultsFullVisualizer" testclass="ResultCollector" testname="View Results Tree" enabled="true">         <boolProp name="ResultCollector.error_logging">false</boolProp>         <objProp>           <name>saveConfig</name>           <value class="SampleSaveConfiguration">             <time>true</time>             <latency>true</latency>             <timestamp>true</timestamp>             <success>true</success>             <label>true</label>             <code>true</code>             <message>true</message>             <threadName>true</threadName>             <dataType>false</dataType>             <encoding>false</encoding>             <assertions>true</assertions>             <subresults>false</subresults>             <responseData>false</responseData>             <samplerData>false</samplerData>             <xml>false</xml>             <fieldNames>true</fieldNames>             <responseHeaders>false</responseHeaders>             <requestHeaders>false</requestHeaders>             <responseDataOnError>true</responseDataOnError>             <saveAssertionResultsFailureMessage>true</saveAssertionResultsFailureMessage>             <assertionsResultsToSave>0</assertionsResultsToSave>             <bytes>true</bytes>             <hostname>true</hostname>             <threadCounts>true</threadCounts>             <sampleCount>true</sampleCount>           </value>         </objProp>         <stringProp name="filename"></stringProp>       </ResultCollector>       <hashTree/>       <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="Thread Group" enabled="true">         <stringProp name="ThreadGroup.on_sample_error">continue</stringProp>         <elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller" enabled="true">           <boolProp name="LoopController.continue_forever">false</boolProp>           <intProp name="LoopController.loops">-1</intProp>         </elementProp>         <stringProp name="ThreadGroup.num_threads">${__P(THREADS)}</stringProp>         <stringProp name="ThreadGroup.ramp_time">${__P(THREADS_RAMPUP_TIME)}</stringProp>         <boolProp name="ThreadGroup.scheduler">false</boolProp>         <stringProp name="ThreadGroup.duration"></stringProp>         <stringProp name="ThreadGroup.delay"></stringProp>         <boolProp name="ThreadGroup.same_user_on_next_iteration">false</boolProp>       </ThreadGroup>       <hashTree/>     </hashTree>   </hashTree> </jmeterTestPlan> '
baseline_jmx = '<?xml version="1.0" encoding="UTF-8"?> <jmeterTestPlan version="1.2" properties="5.0" jmeter="5.2.1">   <hashTree>     <TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="JMeter Test Plan" enabled="true">       <stringProp name="TestPlan.comments"></stringProp>       <boolProp name="TestPlan.functional_mode">false</boolProp>       <boolProp name="TestPlan.serialize_threadgroups">false</boolProp>       <elementProp name="TestPlan.user_defined_variables" elementType="Arguments" guiclass="ArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">         <collectionProp name="Arguments.arguments"/>       </elementProp>       <stringProp name="TestPlan.user_define_classpath"></stringProp>     </TestPlan>     <hashTree>       <CacheManager guiclass="CacheManagerGui" testclass="CacheManager" testname="HTTP Cache Manager" enabled="true">         <boolProp name="clearEachIteration">true</boolProp>         <boolProp name="useExpires">true</boolProp>         <boolProp name="CacheManager.controlledByThread">false</boolProp>       </CacheManager>       <hashTree/>       <Arguments guiclass="ArgumentsPanel" testclass="Arguments" testname="User Defined Variables - EDIT ALL VARIABLES HERE!" enabled="true">         <collectionProp name="Arguments.arguments">           <elementProp name="THREADS" elementType="Argument">             <stringProp name="Argument.name">THREADS</stringProp>             <stringProp name="Argument.value">10</stringProp>             <stringProp name="Argument.metadata">=</stringProp>             <stringProp name="Argument.desc">Change as per requirement</stringProp>           </elementProp>           <elementProp name="THREADS_RAMPUP_TIME" elementType="Argument">             <stringProp name="Argument.name">THREADS_RAMPUP_TIME</stringProp>             <stringProp name="Argument.value">10</stringProp>             <stringProp name="Argument.desc">Valune in seconds - Change as per requirement</stringProp>             <stringProp name="Argument.metadata">=</stringProp>           </elementProp>           <elementProp name="START_TPS" elementType="Argument">             <stringProp name="Argument.name">START_TPS</stringProp>             <stringProp name="Argument.value">5</stringProp>             <stringProp name="Argument.metadata">=</stringProp>           </elementProp>           <elementProp name="END_TPS" elementType="Argument">             <stringProp name="Argument.name">END_TPS</stringProp>             <stringProp name="Argument.value">5</stringProp>             <stringProp name="Argument.metadata">=</stringProp>           </elementProp>           <elementProp name="TEST_DURATION" elementType="Argument">             <stringProp name="Argument.name">TEST_DURATION</stringProp>             <stringProp name="Argument.value">1800</stringProp>             <stringProp name="Argument.metadata">=</stringProp>             <stringProp name="Argument.desc">Valune in seconds - Change as per requirement</stringProp>           </elementProp>         </collectionProp>         <stringProp name="TestPlan.comments">EDIT ALL VARIABLES HERE!</stringProp>       </Arguments>       <hashTree/>       <ResponseAssertion guiclass="AssertionGui" testclass="ResponseAssertion" testname="Global Response Assertion" enabled="true">         <collectionProp name="Asserion.test_strings">           <stringProp name="1538630">20\d</stringProp>         </collectionProp>         <stringProp name="Assertion.custom_message"></stringProp>         <stringProp name="Assertion.test_field">Assertion.response_code</stringProp>         <boolProp name="Assertion.assume_success">false</boolProp>         <intProp name="Assertion.test_type">2</intProp>       </ResponseAssertion>       <hashTree/>       <kg.apc.jmeter.timers.VariableThroughputTimer guiclass="kg.apc.jmeter.timers.VariableThroughputTimerGui" testclass="kg.apc.jmeter.timers.VariableThroughputTimer" testname="LOAD TEST - Throughput Shaping Timer" enabled="true">         <collectionProp name="load_profile">           <collectionProp name="731866749">             <stringProp name="1606799354">${START_TPS}</stringProp>             <stringProp name="779619553">${END_TPS}</stringProp>             <stringProp name="-1857560941">${TEST_DURATION}</stringProp>           </collectionProp>         </collectionProp>       </kg.apc.jmeter.timers.VariableThroughputTimer>       <hashTree/>       <kg.apc.jmeter.timers.VariableThroughputTimer guiclass="kg.apc.jmeter.timers.VariableThroughputTimerGui" testclass="kg.apc.jmeter.timers.VariableThroughputTimer" testname="SOAK TEST - Throughput Shaping Timer" enabled="false">         <collectionProp name="load_profile">           <collectionProp name="731866749">             <stringProp name="1606799354">${START_TPS}</stringProp>             <stringProp name="779619553">${END_TPS}</stringProp>             <stringProp name="-1857560941">${TEST_DURATION}</stringProp>           </collectionProp>         </collectionProp>       </kg.apc.jmeter.timers.VariableThroughputTimer>       <hashTree/>       <kg.apc.jmeter.timers.VariableThroughputTimer guiclass="kg.apc.jmeter.timers.VariableThroughputTimerGui" testclass="kg.apc.jmeter.timers.VariableThroughputTimer" testname="CAPACITY TEST - Throughput Shaping Timer" enabled="false">         <collectionProp name="load_profile">           <collectionProp name="1954571997">             <stringProp name="53">5</stringProp>             <stringProp name="53">5</stringProp>             <stringProp name="53430">600</stringProp>           </collectionProp>           <collectionProp name="1571222845">             <stringProp name="1567">10</stringProp>             <stringProp name="1567">10</stringProp>             <stringProp name="53430">600</stringProp>           </collectionProp>           <collectionProp name="1572182109">             <stringProp name="1572">15</stringProp>             <stringProp name="1572">15</stringProp>             <stringProp name="53430">600</stringProp>           </collectionProp>         </collectionProp>       </kg.apc.jmeter.timers.VariableThroughputTimer>       <hashTree/>       <ResultCollector guiclass="SummaryReport" testclass="ResultCollector" testname="Summary Report" enabled="true">         <boolProp name="ResultCollector.error_logging">false</boolProp>         <objProp>           <name>saveConfig</name>           <value class="SampleSaveConfiguration">             <time>true</time>             <latency>true</latency>             <timestamp>true</timestamp>             <success>true</success>             <label>true</label>             <code>true</code>             <message>true</message>             <threadName>true</threadName>             <dataType>true</dataType>             <encoding>false</encoding>             <assertions>true</assertions>             <subresults>true</subresults>             <responseData>false</responseData>             <samplerData>false</samplerData>             <xml>false</xml>             <fieldNames>true</fieldNames>             <responseHeaders>false</responseHeaders>             <requestHeaders>false</requestHeaders>             <responseDataOnError>false</responseDataOnError>             <saveAssertionResultsFailureMessage>true</saveAssertionResultsFailureMessage>             <assertionsResultsToSave>0</assertionsResultsToSave>             <bytes>true</bytes>             <sentBytes>true</sentBytes>             <threadCounts>true</threadCounts>             <idleTime>true</idleTime>             <connectTime>true</connectTime>           </value>         </objProp>         <stringProp name="filename"></stringProp>       </ResultCollector>       <hashTree/>       <ResultCollector guiclass="ViewResultsFullVisualizer" testclass="ResultCollector" testname="View Results Tree" enabled="true">         <boolProp name="ResultCollector.error_logging">false</boolProp>         <objProp>           <name>saveConfig</name>           <value class="SampleSaveConfiguration">             <time>true</time>             <latency>true</latency>             <timestamp>true</timestamp>             <success>true</success>             <label>true</label>             <code>true</code>             <message>true</message>             <threadName>true</threadName>             <dataType>false</dataType>             <encoding>false</encoding>             <assertions>true</assertions>             <subresults>false</subresults>             <responseData>false</responseData>             <samplerData>false</samplerData>             <xml>false</xml>             <fieldNames>true</fieldNames>             <responseHeaders>false</responseHeaders>             <requestHeaders>false</requestHeaders>             <responseDataOnError>true</responseDataOnError>             <saveAssertionResultsFailureMessage>true</saveAssertionResultsFailureMessage>             <assertionsResultsToSave>0</assertionsResultsToSave>             <bytes>true</bytes>             <hostname>true</hostname>             <threadCounts>true</threadCounts>             <sampleCount>true</sampleCount>           </value>         </objProp>         <stringProp name="filename"></stringProp>       </ResultCollector>       <hashTree/>       <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="Thread Group" enabled="true">         <stringProp name="ThreadGroup.on_sample_error">startnextloop</stringProp>         <elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller" enabled="true">           <boolProp name="LoopController.continue_forever">false</boolProp>           <intProp name="LoopController.loops">-1</intProp>         </elementProp>         <stringProp name="ThreadGroup.num_threads">${THREADS}</stringProp>         <stringProp name="ThreadGroup.ramp_time">${THREADS_RAMPUP_TIME}</stringProp>         <boolProp name="ThreadGroup.scheduler">false</boolProp>         <stringProp name="ThreadGroup.duration"></stringProp>         <stringProp name="ThreadGroup.delay"></stringProp>         <boolProp name="ThreadGroup.same_user_on_next_iteration">false</boolProp>       </ThreadGroup>       <hashTree/>     </hashTree>   </hashTree> </jmeterTestPlan> '
TG_TC_HTTPSampler_jmx = '        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="Request_MY-NAME" enabled="true">           <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>           <elementProp name="HTTPsampler.Arguments" elementType="Arguments">             <collectionProp name="Arguments.arguments">               <elementProp name="" elementType="HTTPArgument">                 <boolProp name="HTTPArgument.always_encode">false</boolProp>                 <stringProp name="Argument.value">MY-BODY</stringProp>                 <stringProp name="Argument.metadata">=</stringProp>               </elementProp>             </collectionProp>           </elementProp>           <stringProp name="HTTPSampler.domain"></stringProp>           <stringProp name="HTTPSampler.port"></stringProp>           <stringProp name="HTTPSampler.protocol"></stringProp>           <stringProp name="HTTPSampler.contentEncoding"></stringProp>           <stringProp name="HTTPSampler.path">MY-PATH</stringProp>           <stringProp name="HTTPSampler.method">MY-METHOD</stringProp>           <boolProp name="HTTPSampler.follow_redirects">true</boolProp>           <boolProp name="HTTPSampler.auto_redirects">false</boolProp>           <boolProp name="HTTPSampler.use_keepalive">true</boolProp>           <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>           <stringProp name="HTTPSampler.embedded_url_re"></stringProp>           <stringProp name="HTTPSampler.connect_timeout"></stringProp>           <stringProp name="HTTPSampler.response_timeout"></stringProp>         </HTTPSamplerProxy>'
headerStringStart_jmx = '          <hashTree>             <HeaderManager guiclass="HeaderPanel" testclass="HeaderManager" testname="HTTP Header Manager" enabled="true">               <collectionProp name="HeaderManager.headers">'
headerStringEnd_jmx = '              </collectionProp>             </HeaderManager>             <hashTree/>           </hashTree>'
itr_jmx = ''
itr_final_jmx = ''

########### Code  #########

inputpath = input("Enter file path where postman collection is parked along with environment variables and/or global variables if defined : ")
#variablefile = input("If you have defined variables in postman, please export variables for the environment where you would like to run performance test and provide exported file path here, in case no variable defined just press Enter key\nEnter variables file path : ")

# print(os.getcwd())

try:
    for i in os.listdir(inputpath):
         # print(i)
         if "collection" in i:
            inputfile = inputpath+"\\"+i
         if "environment" in i:
            variablefile = inputpath+"\\"+i
         if "globals" in i:
            globalvariablefile = inputpath+"\\"+i
except Exception as e:
    logging.error('Something went wrong with path provided, please verify path' + str(e))
    sys.exit(1)

dirname = os.path.dirname(inputfile)
outfile = dirname+'\\YourJMeterScript.jmx'

try:
    with open(inputfile, 'r') as rf:
        FileContent = rf.read().replace('\n','')
        FileContent = FileContent.replace('\t', '')
        splitFile = FileContent.split('"schema"')
        filePart_1 = splitFile[0]
        filePart_2 = splitFile[1]
        # print(filePart_2)
except Exception as e:
    logging.error('Something went wrong while opening postman collection' + str(e))
    sys.exit(1)

findRequests = re.findall(r'{"name": "(.*?)",(.*?)"response"',filePart_2, re.DOTALL)

num = 0

for i in findRequests:
    # print(i[1])
    num = num + 1

    temp_jmx = ''
    headerStringMid_jmx = ''

    #Name
    searchName = re.findall(r'{"name": "(.*?)",', i[1], re.DOTALL)
    mylen = len(searchName) - 1

    if mylen >= 0:
        # print(searchName[mylen])
        myName = searchName[mylen]
    else:
        myName = i[0]
        # print(myName)
    myNameUpdated = str(num) + '_' + myName
    temp_jmx = TG_TC_HTTPSampler_jmx.replace('MY-NAME',myNameUpdated)

    #method
    searchMethod = re.search(r'"method": "(.*?)"',i[1])
    myMethod = searchMethod.group(1)

    temp_jmx = temp_jmx.replace('MY-METHOD',myMethod)

    #url
    searchURL = re.search(r'"url": "(.*?)"', i[1])
    if searchURL == None:
        searchURL = re.search(r'"url": {(.*?)": "(.*?)",', i[1])
        myURL = re.sub('&','&amp;',searchURL.group(2))
    else:
        myURL = re.sub('&', '&amp;', searchURL.group(1))

    temp_jmx = temp_jmx.replace('MY-PATH', myURL)

    #Body
    searchBody = re.search(r'"body": {"mode": "raw","raw": "(.*?)","options', i[1])

    if searchBody != None:
        myRequestBody = searchBody.group(1)
        myRequestBody = re.sub('<','&lt;',myRequestBody)
        myRequestBody = re.sub('>','&gt;',myRequestBody)
        myRequestBody = re.sub(r'\\"','&quot;',myRequestBody)
        # myRequestBody = re.sub(r'\\t','',myRequestBody)
        myRequestBody = myRequestBody.replace("\\r\\n", "\n")

    else:
        myRequestBody= ''

    temp_jmx= temp_jmx.replace('MY-BODY', myRequestBody)

    #Headers
    searchHeaders = re.search (r'"header": \[(.*?)\]',i[1])

    myHeaders = searchHeaders.group(1)
    # print(myHeaders)
    findHeaders_all = re.findall(r'{"(.*?)}', myHeaders, re.DOTALL)
    # findHeaders_all = re.findall(r'{"(.*?)"}',myHeaders, re.DOTALL)
    # print(findHeaders_all)
    # print(len(findHeaders_all))
    # findHeaders_all = re.findall(r'(.*?)', myHeaders, re.DOTALL)
    myHeaders_updated = list()

    for i in findHeaders_all:

        i = i+'"'
        # print(i)
        searchDisabled_Header = re.search(r'"disabled": true', i)
        if searchDisabled_Header == None:
            scanHeaders1 = re.search('key": "(.*?)"(.*?)"value": "(.*?)"', i)
            head = (scanHeaders1.group(1), scanHeaders1.group(3))
            headerToAdd_jmx = '                <elementProp name="" elementType="Header">                   <stringProp name="Header.name">'+scanHeaders1.group(1)+'</stringProp>                   <stringProp name="Header.value">'+scanHeaders1.group(3)+'</stringProp>                 </elementProp>'
            headerStringMid_jmx = headerStringMid_jmx + headerToAdd_jmx

            myHeaders_updated.append(head)

    header_JMX = headerStringStart_jmx + headerStringMid_jmx + headerStringEnd_jmx
    # print(header_JMX)
    itr_jmx = temp_jmx + header_JMX

    itr_final_jmx = itr_final_jmx + itr_jmx



baseline_jmx_find = '</ThreadGroup>       <hashTree/>     </hashTree>   </hashTree> </jmeterTestPlan>'
baseline_jmx_replace = '</ThreadGroup>'+ '<hashTree>'+ itr_final_jmx + '</hashTree>'+ '</hashTree>   </hashTree> </jmeterTestPlan>'
output = baseline_jmx.replace(baseline_jmx_find,baseline_jmx_replace)

# Environment Variables
try:
    with open(variablefile, 'r') as rf:
        FileContent = rf.read().replace('\n','')
        FileContent = FileContent.replace('\t', '')
        findVariables = re.findall(r'"key": "(.*?)","value": "(.*?)"', FileContent, re.DOTALL)

        current_UDV = re.search(r'<collectionProp name="Arguments.arguments">(.*?)</collectionProp>', output)
        # print(current_UDV.group(1))

        imported_UDV = ''

        for i in findVariables:

            myStr = '<elementProp name="'+i[0]+'" elementType="Argument">            <stringProp name="Argument.name">'+i[0]+'</stringProp>            <stringProp name="Argument.value">'+i[1]+'</stringProp>            <stringProp name="Argument.metadata">=</stringProp>            <stringProp name="Argument.desc">Imported from environment variables </stringProp>          </elementProp>'
            imported_UDV = imported_UDV + myStr

            to_find = '{{'+i[0]+'}}'
            to_replace = '${'+i[0]+'}'
            output = output.replace(to_find,to_replace)

        final_UDV = current_UDV.group(1) + imported_UDV
        # print(final_UDV)
        output = output.replace(current_UDV.group(1),final_UDV)

except Exception as e:
    logging.info('Either environment variables file not provided or something went wrong while opening it! ' + str(e))

# global variables
try:
    with open(globalvariablefile, 'r') as rf:
        FileContent = rf.read().replace('\n','')
        FileContent = FileContent.replace('\t', '')
        findVariables = re.findall(r'"key": "(.*?)","value": "(.*?)"', FileContent, re.DOTALL)

        current_UDV = re.search(r'<collectionProp name="Arguments.arguments">(.*?)</collectionProp>', output)
        # print(current_UDV.group(1))

        imported_UDV = ''

        for i in findVariables:
            # print(i)
            myStr = '<elementProp name="'+i[0]+'" elementType="Argument">            <stringProp name="Argument.name">'+i[0]+'</stringProp>            <stringProp name="Argument.value">'+i[1]+'</stringProp>            <stringProp name="Argument.metadata">=</stringProp>            <stringProp name="Argument.desc">Imported from global variables </stringProp>          </elementProp>'
            imported_UDV = imported_UDV + myStr

            to_find = '{{'+i[0]+'}}'
            to_replace = '${'+i[0]+'}'
            output = output.replace(to_find,to_replace)

        final_UDV = current_UDV.group(1) + imported_UDV
        # print(final_UDV)
        output = output.replace(current_UDV.group(1),final_UDV)

except Exception as e:
    logging.info('Either global variables file not provided or something went wrong while opening it! ' + str(e))

try:
    with open (outfile,'w+') as wf:
        wf.write(output)
        logging.info('Successfully created jmeter JMX file & Parked at location: ' +outfile)
except Exception as e:
    logging.error('Something went wrong while opening output file' + str(e))
    sys.exit()