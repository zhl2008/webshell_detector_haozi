#!/usr/bin/env python

check_hash_span = 1

time_span = 0.25

max_directory_depth = 4

max_file_size = 102400 * 3

max_regrex_file_size = 102400/2

max_monitor_file_size = 102400 * 10

rule_hit = {}

file_match_rule = {}

init_rules = {'cc2ed3c634877bf77ab563a576a645b7': 1, '9c6f68b9cdc3f56ece96e64c0a43b802': 1, '52de3a486e729952f541514cee81c626': 1, '6fbb86a13329fcf0710d72b1c92b8f1f': 1, 'fa0d6ae87b688eb1986b753edb6533e1': 1, '4626a35a053002518fd540b3505c861e': 1, '00c5101394a758851d1486cbeee26bb2': 1, '03b20d4b548d221527941d1a6098ddd3': 1, '62f74a60fdc94bf7dfca05a50c52d086': 1, '3c1c42ef2937491f9fe60dc898e7e987': 1, '66f0e49ca4da92188ce1e53a80172358': 1, 'da4dd29daea6716bb494381a75540ea5': 1, 'cbba5854b6b4d37f3be08e8bf0045c6c': 1, 'c553ba9d158478f0a8617a0eeef8d24a': 1, '7e06b788274b10f96010073344aff5ee': 1, 'e77917c4ec8e9172394ccd71527fcadd': 1, '17718597d74d40bb539aea17b9945ce6': 1, '647850d7754d20dd3574104b71148dcb': 1, 'c78557ba9b5a274416f733a4d5b8a00a': 1, '34ef5c62729c20d351d20faed7d18a5c': 1, 'b4a2eea6e8458dcbaaf9573715ea8126': 1, '2f02be11a401d90bab21733c699ea3bb': 1, '357781c5a932ca2628811a6d946ea14e': 1, 'ca731f9344e7b1617779c8c5c57e98bf': 1, '28adfde217f1eec9d859284f04a5c975': 1, '02792377af943fa68847509baef3fb8a': 1, '7ea9ca2ccc7ad81bb856dd7ca743ea02': 1, '22fb7da32fecf8391492e8c03d5e8771': 1, '4e08b978297e7d567d55b1a389414b24': 1, '473f7ffaf345d097256a927eccaf6a28': 1, '0db5a958192b1cbda2f3142c123d7571': 1, 'b7ff4d39af195ee9c55e0c558b1e120b': 1, 'abdc071f6ac076ffd4a69bcc3ce61c67': 1, '24650e301216120b349fdd17c02f9e6c': 1, '38e2135f2ab85d315c7c5a81662d7167': 1, 'edc0b9b448d237b6f6164196aac9b7e5': 1, '876f2c97f0239020d117ffc0e220e4d2': 1, '6ac60864fdfee534957d7883478c640c': 1, 'cb26348f28e42d72366dcac90eb1f833': 1, '14c5932fe3de433a3f02f6ed4d190d45': 1, 'd6fcb63fe4b4b6afb18e7d4166531ba9': 1, '7196170cdfa81aba87b52b7abf9798e2': 1, '1a80400a03c19c34fdeda28c024eaf39': 1, '99fb01ae0b05d4c15be8b1a3afa5b535': 1, '8f4936baad91e9ced91a449c2db17712': 1, '599304504d3c2b120af9a010260b5d2e': 1, '1101f9a1764d38a079c560b12831ccff': 1, '560f447b2f91de93979ea768fc7b88e1': 1, '781ac1b9820d0e653c75102d1a5eca88': 1, '6ee9d596d07702be99d23e015ba9322a': 1, 'b021a7713d6eb2499aabb17820c483ec': 1, 'a77a3344ffdff81e1bdf356275f5cdbf': 1, 'd3044224040076e98bd5654f942c232f': 1, '3831555ec43643056b2bc0c90772a8c6': 1, '5870ee0500793546c4861958c9b71a69': 1, '1464ae029be6efe64f903b2232706ce1': 1, '2f62094d4856acd13feb1da7a3c0e70b': 1, 'b08b00aad4568a8149591df47c75aa8a': 1, '00db30ab658c03f6aba704bb2dde598e': 1, '56913ba09290dc1f6a6758d71ac732d8': 1, 'b96a67ca2d9a5d840be5bae87fc6f14f': 1, '6eb8dace678bfa25242153288bcee3b3': 1, '0686aff3fa6b7a0e7adc0cdfc1f5df55': 1}
webshell_rules = {'cc2ed3c634877bf77ab563a576a645b7': [{'type': '2', 'data': 'File('}, {'type': '2', 'data': 'PrintWriter('}, {'type': '2', 'data': '.println('}, {'type': '2', 'data': '.exists('}, {'type': '2', 'data': '.length('}, {'type': '2', 'data': 'request.getRequestURI()'}, {'type': '2', 'data': 'response.sendRedirect('}, {'type': '2', 'data': 'request.getRealPath(request.getServletPath())'}], '9c6f68b9cdc3f56ece96e64c0a43b802': [{'data': 'java\\.net\\.URLClassLoader', 'type': '1'}], '52de3a486e729952f541514cee81c626': [{'type': '2', 'data': 'publicclassListServletextendsHttpServlet\n\n{publicvoid'}, {'type': '2', 'data': '.getWriter()'}, {'type': '2', 'data': 'if(req.getParameter("")==null)'}, {'type': '2', 'data': 'newFile('}, {'type': '2', 'data': '.isDirectory()){'}, {'type': '2', 'data': '.listFiles();for(int'}, {'type': '2', 'data': '[].isDirectory()){'}, {'type': '2', 'data': '[].isFile())'}, {'type': '2', 'data': 'newFileInputStream('}], '03b20d4b548d221527941d1a6098ddd3': [{'type': '2', 'data': 'request.getRequestURI()'}, {'type': '2', 'data': 'application.getRealPath('}, {'type': '2', 'data': 'newFile'}, {'type': '2', 'data': 'newPrintWriter('}, {'type': '2', 'data': '.exists('}, {'type': '2', 'data': '.length()>)'}, {'type': '2', 'data': '.printStackTrace()'}], 'fa0d6ae87b688eb1986b753edb6533e1': [{'type': '2', 'data': 'newInstance();'}, {'type': '2', 'data': 'DriverManager.getConnection('}, {'type': '2', 'data': '.createStatement('}, {'type': '2', 'data': '.executeQuery('}], '4626a35a053002518fd540b3505c861e': [{'type': '2', 'data': 'Runtime.getRuntime()'}, {'type': '2', 'data': '.exec('}], '00db30ab658c03f6aba704bb2dde598e': [{'type': '2', 'data': 'isNotEmpty(getSystemEncoding())'}, {'type': '2', 'data': '.printStackTrace(newPrintWriter('}, {'type': '2', 'data': 'getSystemEncoding('}, {'type': '2', 'data': 'ByteArrayOutputStream('}, {'type': '2', 'data': '.delete()'}, {'type': '2', 'data': 'exec('}, {'type': '2', 'data': 'isNotEmpty(request.getParameter('}, {'type': '2', 'data': '.getBytes('}, {'type': '2', 'data': 'BufferedOutputStream(response.getOutputStream())\n\n'}, {'type': '2', 'data': '.pushBody()'}], '22fb7da32fecf8391492e8c03d5e8771': [{'data': 'Runtime\\.getRuntime\\(\\)\\.exec', 'type': '1'}], '62f74a60fdc94bf7dfca05a50c52d086': [{'type': '2', 'data': 'convertpath(application.getrealpath(""));'}, {'type': '2', 'data': 'application.getrealpath(request.getrequesturi())\n\n'}, {'type': '2', 'data': '.getParent();session.setMaxInactiveInterval()'}, {'type': '2', 'data': 'StringencodeGbUnicode('}, {'type': '2', 'data': 'newFile('}, {'type': '2', 'data': '.isHidden()'}, {'type': '2', 'data': 'newSimpleDateFormat('}, {'type': '2', 'data': 'out.print("");out.print("");out.print("");out.print\n\n("");out.print("");out.print("");'}], '3c1c42ef2937491f9fe60dc898e7e987': [{'type': '2', 'data': 'DriverManager.getConnection'}, {'type': '2', 'data': '.prepareStatement('}, {'type': '2', 'data': '.executeQuery('}, {'type': '2', 'data': 'ArrayList<String>'}, {'type': '2', 'data': 'newArrayList<String>();while(rs.next())'}, {'type': '2', 'data': 'newOutputStreamWriter(newFileOutputStream('}, {'type': '2', 'data': '.prepareStatement('}, {'type': '2', 'data': '.executeQuery()'}, {'type': '2', 'data': '.getColumnCount('}, {'type': '2', 'data': '.printStackTrace('}], '66f0e49ca4da92188ce1e53a80172358': [{'type': '2', 'data': 'DateFormat.getDateTimeInstance()'}, {'type': '2', 'data': 'System.currentTimeMillis()'}, {'type': '2', 'data': 'convertFileSize('}, {'type': '2', 'data': 'System.arraycopy('}, {'type': '2', 'data': 'newHashtable('}, {'type': '2', 'data': 'System.getProperty('}, {'type': '2', 'data': 'IllegalArgumentException'}, {'type': '2', 'data': '.startsWith('}, {'type': '2', 'data': 'IllegalArgumentException('}, {'type': '2', 'data': '.nextToken('}, {'type': '2', 'data': '.nextToken().trim().equalsIgnoreCase('}, {'type': '2', 'data': 'FileOutputStream('}, {'type': '2', 'data': '.separatorChar'}, {'type': '2', 'data': 'URLDecoder.decode('}, {'type': '2', 'data': '.append(conv2Html('}, {'type': '2', 'data': '.getCanonicalPath().startsWith('}, {'type': '2', 'data': '.getAbsolutePath()'}, {'type': '2', 'data': '.getParameterValues('}, {'type': '2', 'data': '.getAbsolutePath('}, {'type': '2', 'data': 'FileOutputStream('}, {'type': '2', 'data': 'GZIPInputStream('}, {'type': '2', 'data': 'application.getRealPath(request.getRequestURI())).getParent\n\n()'}], 'da4dd29daea6716bb494381a75540ea5': [{'type': '2', 'data': 'initPageData(request,session);'}, {'type': '2', 'data': 'if(request.getParameter('}, {'type': '2', 'data': 'DataBaseType.equalsIgnoreCase('}, {'type': '2', 'data': 'DriverManager.getConnection('}, {'type': '2', 'data': '.prepareStatement('}, {'type': '2', 'data': '.printStackTrace()'}, {'type': '2', 'data': 'session.setAttribute('}, {'type': '2', 'data': '.equals(request.getParameter('}, {'type': '2', 'data': 'setConnection(request,session);'}, {'type': '2', 'data': 'executQuery(connection,SHOWDATEBASES);'}, {'type': '2', 'data': '(HttpServletRequest'}, {'type': '2', 'data': 'executQuery('}, {'type': '2', 'data': '.getColumnName('}, {'type': '2', 'data': '.getMetaData('}, {'type': '2', 'data': 'session.setAttribute('}], 'cbba5854b6b4d37f3be08e8bf0045c6c': [{'type': '2', 'data': 'publicclasscmdservletextendshttpservlet\n\n{publicvoid'}, {'type': '2', 'data': '.getWriter()'}, {'type': '2', 'data': 'runtime.getruntime().exec(""\\+req.getparameter\n\n(""));'}, {'type': '2', 'data': 'ewDataInputStream('}, {'type': '2', 'data': '.print((char)'}], 'c553ba9d158478f0a8617a0eeef8d24a': [{'data': '(java\\.sql\\.)?DriverManager\\.(getConnection|registerDriver)\\(.*?\\)', 'type': '1'}], '7e06b788274b10f96010073344aff5ee': [{'data': 'new\\s*(java\\.io\\.)?ProcessBuilder\\(.*?\\)', 'type': '1'}], 'e77917c4ec8e9172394ccd71527fcadd': [{'type': '2', 'data': 'System.currentTimeMillis()'}, {'type': '2', 'data': 'System.getProperties();'}, {'type': '2', 'data': '.hasMoreElements('}, {'type': '2', 'data': '.indexOf('}, {'type': '2', 'data': '.put('}, {'type': '2', 'data': 'Random().nextInt('}, {'type': '2', 'data': 'request.getQueryString().indexOf('}, {'type': '2', 'data': '(float)Runtime.getRuntime().freeMemory()'}, {'type': '2', 'data': '(float)Runtime.getRuntime().totalMemory()'}, {'type': '2', 'data': '.htShowMsg.get('}, {'type': '2', 'data': '.htShowMsg.get('}], '17718597d74d40bb539aea17b9945ce6': [{'type': '2', 'data': 'IllegalArgumentException('}, {'type': '2', 'data': 'boundary.trim().length()'}, {'type': '2', 'data': 'Hashtable('}, {'type': '2', 'data': 'StringTokenizer('}, {'type': '2', 'data': '.nextToken('}, {'type': '2', 'data': '.lastIndexOf('}, {'type': '2', 'data': '.isDirectory('}, {'type': '2', 'data': 'ZipEntry('}, {'type': '2', 'data': 'BufferedInputStream(newFileInputStream('}, {'type': '2', 'data': '.getAbsolutePath()=conv2Html('}, {'type': '2', 'data': 'response.setContentType('}, {'type': '2', 'data': 'conv2Html(request.getParameter('}, {'type': '2', 'data': '.getName('}, {'type': '2', 'data': ').createNewFile('}], '647850d7754d20dd3574104b71148dcb': [{'type': '2', 'data': 'ExeShellResultshellResult=newExeShellResult();'}, {'type': '2', 'data': 'ExeShellCmd.exec('}], 'c78557ba9b5a274416f733a4d5b8a00a': [{'type': '2', 'data': ').newInstance('}, {'type': '2', 'data': 'DriverManager.getConnection('}, {'type': '2', 'data': '.setCatalog('}, {'type': '2', 'data': 'File.listRoots('}, {'type': '2', 'data': '.listFiles('}, {'type': '2', 'data': '.lastModified('}, {'type': '2', 'data': '.isDirectory('}, {'type': '2', 'data': '.getName('}, {'type': '2', 'data': '.append('}, {'type': '2', 'data': '.delete('}, {'type': '2', 'data': '.getOutputStream('}, {'type': '2', 'data': 'FileInputStream('}, {'type': '2', 'data': '.createNewFile('}, {'type': '2', 'data': 'SimpleDateFormat('}, {'type': '2', 'data': '(HttpURLConnection)'}, {'type': '2', 'data': '.getMetaData().getTables('}, {'type': '2', 'data': '.createStatement('}, {'type': '2', 'data': '.executeQuery('}, {'type': '2', 'data': 'Runtime.getRuntime().exec('}, {'type': '2', 'data': '.getInputStream('}], '34ef5c62729c20d351d20faed7d18a5c': [{'type': '2', 'data': '.hasMoreElements()){String'}, {'type': '2', 'data': 'request.getHeader('}, {'type': '2', 'data': '.setProperty(('}, {'type': '2', 'data': ').toLowerCase()'}, {'type': '2', 'data': '.equalsIgnoreCase('}, {'type': '2', 'data': 'request.getInputStream()'}, {'type': '2', 'data': '.delete()'}, {'type': '2', 'data': '.read())'}], 'b4a2eea6e8458dcbaaf9573715ea8126': [{'type': '2', 'data': 'allowTypes=newString[]{"jpg","jpeg","gif","ico","bmp","png"}\n\n'}, {'type': '2', 'data': 'Util.null2String(request.getParameter("dir"));'}, {'type': '2', 'data': 'saveFile.substring(0,saveFile.indexOf('}, {'type': '2', 'data': 'newFileOutputStream(fileName);'}], '2f02be11a401d90bab21733c699ea3bb': [{'type': '2', 'data': 'HttpServletRequest'}, {'type': '2', 'data': '.getBytes(REQUEST_CHARSET)'}, {'type': '2', 'data': '.getConnection('}, {'type': '2', 'data': '.isClosed('}, {'type': '2', 'data': '.url.equals('}, {'type': '2', 'data': 'InputStreamReader('}, {'type': '2', 'data': 'OutputStreamWriter('}, {'type': '2', 'data': '.write('}, {'type': '2', 'data': '.flush('}, {'type': '2', 'data': '.toLowerCase().endsWith('}, {'type': '2', 'data': 'JarFile('}, {'type': '2', 'data': 'ZipFile('}, {'type': '2', 'data': 'EnterFile('}, {'type': '2', 'data': '.setAbsolutePath('}, {'type': '2', 'data': '.getMetaData('}, {'type': '2', 'data': '.getColumnName('}, {'type': '2', 'data': 'formatNumber('}, {'type': '2', 'data': '.getInterfaces().length'}, {'type': '2', 'data': 'response.getOutputStream('}], '357781c5a932ca2628811a6d946ea14e': [{'data': 'new\\s*(java\\.net\\.)?Socket\\(.*?\\)', 'type': '1'}], 'ca731f9344e7b1617779c8c5c57e98bf': [{'type': '2', 'data': 'javax.servlet.http.HttpServletRequest'}, {'type': '2', 'data': 'com.caucho.jsp.QPageContext'}, {'type': '2', 'data': 'pageContext.getSession();'}, {'type': '2', 'data': 'pageContext.getServletContext();'}, {'type': '2', 'data': 'com.caucho.util.CauchoSystem.getResinHome();'}, {'type': '2', 'data': 'com.caucho.java.LineMap('}, {'type': '2', 'data': 'com.caucho.vfs.Depend(mergePath.lookup('}], '28adfde217f1eec9d859284f04a5c975': [{'type': '2', 'data': '=Runtime.getRuntime().exec("cmd.exe'}, {'type': '2', 'data': 'Stringcmd=request.getParameter("cmd");'}, {'type': '2', 'data': 'newBufferedReader(newInputStreamReader('}], '1101f9a1764d38a079c560b12831ccff': [{'data': '(\\.(listFiles|list|listRoots)\\s*\\(.+\\.(readLine|read)\\s*\\(.+\\.write\\s*\\()|(\\.(readLine|read)\\s*\\(.+\\.write\\s*\\(.+\\.(listFiles|list|listRoots)\\s*\\()', 'type': '1'}], '7ea9ca2ccc7ad81bb856dd7ca743ea02': [{'type': '1', 'data': '.*FileOutputStream\\(.*request\\.getParameter'}], 'cb26348f28e42d72366dcac90eb1f833': [{'type': '2', 'data': 'newFile(request.getParameter(""))'}, {'type': '2', 'data': '.isDirectory()'}, {'type': '2', 'data': '.listFiles();for('}, {'type': '2', 'data': '.isDirectory('}, {'type': '2', 'data': '[].canRead()==true'}, {'type': '2', 'data': 'response.getOutputStream()'}, {'type': '2', 'data': '.read();'}, {'type': '2', 'data': '.printStackTrace('}], '4e08b978297e7d567d55b1a389414b24': [{'data': 'COM\\.ibm\\.db2\\.jdbc\\.app\\.DB2Driver|COM\\.ibm\\.db2\\.jdbc\\.DB2XADataSource|COM\\.ibm\\.db2\\.jdbc\\.net\\.DB2Driver|com\\.informix\\.jdbc\\.IfxDriver|com\\.informix\\.jdbcx\\.IfxXADataSource|org\\.apache\\.derby\\.jdbc\\.ClientDriver|com\\.microsoft\\.sqlserver\\.jdbc\\.SQLServerDriver|com\\.microsoft\\.jdbc\\.sqlserver\\.SQLServerDriver|com\\.mysql\\.jdbc\\.Driver|org\\.gjt\\.mm\\.mysql\\.Driver|oracle\\.jdbc\\.driver\\.OracleDriver|oracle\\.jdbc\\.xa\\.client\\.OracleXADataSource|oracle\\.jdbc\\.driver\\.OracleDriver|oracle\\.jdbc\\.xa\\.client\\.OracleXADataSource|com\\.tongweb\\.jdbc\\.OracleDriverWrapper|org\\.postgresql\\.Driver|com\\.sybase\\.jdbc\\.SybDriver|com\\.sybase\\.jdbc2\\.jdbc\\.SybXADataSource|org\\.hsqldb\\.jdbcDriver|com\\.sybase\\.jdbc3\\.jdbc\\.SybDriver|com\\.kingbase\\.Driver|dm\\.jdbc\\.driver\\.DmDriver', 'type': '1'}], '560f447b2f91de93979ea768fc7b88e1': [{'type': '2', 'data': 'if(request.getParameter("")=null)'}, {'type': '2', 'data': 'newString(request.getParameter("").getBytes\n\n(""),"");'}, {'type': '2', 'data': 'newFileOutputStream('}, {'type': '2', 'data': 'request.getServerName()'}, {'type': '2', 'data': '.print(request.getRealPath(request.getServletPath()))\n\n'}], '0db5a958192b1cbda2f3142c123d7571': [{'type': '2', 'data': 'publicclassUpServletextendsHttpServlet{'}, {'type': '2', 'data': '.setContentType('}, {'type': '2', 'data': '.getWriter()'}, {'type': '2', 'data': 'out.print("");out.print("");out.print("");'}, {'type': '2', 'data': 'newDataInputStream('}, {'type': '2', 'data': 'newFile('}, {'type': '2', 'data': '.getContentLength()'}, {'type': '2', 'data': '.read();'}, {'type': '2', 'data': '.write((char)'}], 'b7ff4d39af195ee9c55e0c558b1e120b': [{'type': '2', 'data': 'request.getParameter("")'}, {'type': '2', 'data': '=request.getRealPath(request.getServletPath())'}, {'type': '2', 'data': 'newFile('}, {'type': '2', 'data': 'newPrintWriter('}, {'type': '2', 'data': '.length()>'}, {'type': '2', 'data': 'out.println("");out.println("");out.println("")'}], '5870ee0500793546c4861958c9b71a69': [{'type': '2', 'data': 'Runtime.getRuntime()'}, {'type': '2', 'data': 'InputStreamReader('}, {'type': '2', 'data': 'Charset.forName('}, {'type': '2', 'data': 'File('}, {'type': '2', 'data': 'getParent('}, {'type': '2', 'data': '.isDirectory('}, {'type': '2', 'data': '.list()'}, {'type': '2', 'data': '.lastIndexOf('}, {'type': '2', 'data': '.substring('}, {'type': '2', 'data': '.write('}, {'type': '2', 'data': '.isDirectory('}, {'type': '2', 'data': '[request.getContentLength()]'}, {'type': '2', 'data': 'JshellConfigException'}, {'type': '2', 'data': '(String)session.getAttribute('}, {'type': '2', 'data': 'session.removeAttribute('}, {'type': '2', 'data': 'response.sendRedirect(request.getRequestURI())'}, {'type': '2', 'data': 'System.getProperty('}, {'type': '2', 'data': 'request.getRealPath(request.getServletPath())'}], '24650e301216120b349fdd17c02f9e6c': [{'type': '2', 'data': 'Class.forName('}, {'type': '2', 'data': 'DriverManager.getConnection('}, {'type': '2', 'data': 'SimpleDateFormat('}, {'type': '2', 'data': '.isDirectory('}, {'type': '2', 'data': 'HttpServletResponse'}, {'type': '2', 'data': 'BufferedInputStream(newFileInputStream('}, {'type': '2', 'data': 'File('}, {'type': '2', 'data': '.mkdir('}, {'type': '2', 'data': '.listFiles('}, {'type': '2', 'data': '.setLastModified('}, {'type': '2', 'data': 'File(application.getRealPath(request.getRequestURI\n\n())).getParent()'}, {'type': '2', 'data': '.getErrorStream('}], '38e2135f2ab85d315c7c5a81662d7167': [{'type': '2', 'data': 'request.getRequestURI('}, {'type': '2', 'data': '.getBytes('}, {'type': '2', 'data': '.getServletContext().getRealPath('}, {'type': '2', 'data': 'FileReader('}, {'type': '2', 'data': 'FileWriter('}, {'type': '2', 'data': '.replaceAll('}, {'type': '2', 'data': '.queryHashtable('}, {'type': '2', 'data': '.listFiles('}, {'type': '2', 'data': '.getFilePointer('}, {'type': '2', 'data': '.delete('}, {'type': '2', 'data': 'RandomAccessFile('}, {'type': '2', 'data': 'System.out.println('}], 'edc0b9b448d237b6f6164196aac9b7e5': [{'type': '2', 'data': 'extendsJPanelimplementsRunnable'}, {'type': '2', 'data': 'JScrollPanescrollPane'}, {'type': '2', 'data': 'Color('}, {'type': '2', 'data': '.getSystemState('}, {'type': '2', 'data': 'PySystemState'}, {'type': '2', 'data': 'BorderLayout()'}, {'type': '2', 'data': 'Java2DTextWindow('}, {'type': '2', 'data': '.setBackground('}, {'type': '2', 'data': '.setViewportView('}, {'type': '2', 'data': 'DefaultConsoleImpl('}, {'type': '2', 'data': '.setTextAttributes('}, {'type': '2', 'data': 'TextAttributes('}, {'type': '2', 'data': 'setTextAttributes('}, {'type': '2', 'data': '.printStackTrace()'}, {'type': '2', 'data': 'PySystemState.initialize(System.getProperties()'}], '876f2c97f0239020d117ffc0e220e4d2': [{'data': '(?:(?:java\\.lang\\.reflect\\.)?Method)?\\s*(\\w+)\\s*=\\s*.*\\.getMethod\\([\\s\\S]*\\1\\.invoke\\(.*?\\)', 'type': '1'}], '6ac60864fdfee534957d7883478c640c': [{'type': '2', 'data': 'StreamConnectorextendsThread'}, {'type': '2', 'data': 'OutputStream'}, {'type': '2', 'data': 'BufferedReader(newInputStreamReader('}, {'type': '2', 'data': '.read('}, {'type': '2', 'data': '.write('}, {'type': '2', 'data': '.flush()'}, {'type': '2', 'data': '.start()'}, {'type': '2', 'data': '.getInputStream()'}, {'type': '2', 'data': 'request.getParameter('}, {'type': '2', 'data': 'Socket('}], '6eb8dace678bfa25242153288bcee3b3': [{'data': 'new\\s*(java\\.net\\.)?InetSocketAddress\\(.*?\\)', 'type': '1'}], '14c5932fe3de433a3f02f6ed4d190d45': [{'type': '2', 'data': 'Runtime.getRuntime().exec('}], '6fbb86a13329fcf0710d72b1c92b8f1f': [{'type': '2', 'data': 'ByteArrayOutputStream('}, {'type': '2', 'data': 'publicByteArrayOutputStreamgetProgOutput('}, {'type': '2', 'data': 'CopyThread'}, {'type': '2', 'data': '.getErrorStream()'}, {'type': '2', 'data': 'BufferedWriter(newOutputStreamWriter('}, {'type': '2', 'data': 'session.getAttribute('}, {'type': '2', 'data': '.equalsIgnoreCase(function)'}, {'type': '2', 'data': 'request.getParameter('}, {'type': '2', 'data': 'MessageDigest.getInstance('}, {'type': '2', 'data': '.equalsIgnoreCase('}], '7196170cdfa81aba87b52b7abf9798e2': [{'data': '(\\\\u00\\w\\w){3,}', 'type': '1'}], 'b08b00aad4568a8149591df47c75aa8a': [{'data': 'new\\s*(java\\.io\\.)?(FileOutputStream|PrintWriter|FileWriter|RandomAccessFile)\\(.*?\\)', 'type': '1'}], '99fb01ae0b05d4c15be8b1a3afa5b535': [{'type': '2', 'data': 'DriverManager.getConnection'}, {'type': '2', 'data': '.createStatement('}, {'type': '2', 'data': '.executeQuery('}, {'type': '2', 'data': '.getMetaData('}, {'type': '2', 'data': 'response.setStatus()'}, {'type': '2', 'data': 'newOutputStreamWriter(newFileOutputStream('}], '8f4936baad91e9ced91a449c2db17712': [{'type': '2', 'data': 'Runtime.getRuntime().freeMemory();'}, {'type': '2', 'data': 'request.getRequestURI()'}, {'type': '2', 'data': '.remove('}, {'type': '2', 'data': '.get('}, {'type': '2', 'data': 'System.arraycopy('}, {'type': '2', 'data': 'ServletInputStream'}, {'type': '2', 'data': 'IllegalArgumentException'}, {'type': '2', 'data': '.listFiles()'}, {'type': '2', 'data': 'newBufferedReader(newInputStreamReader(newFileInputStream\n\n('}, {'type': '2', 'data': 'newBufferedWriter(newOutputStreamWriter(newFileOutputStream\n\n('}, {'type': '2', 'data': '.mkdirs())'}, {'type': '2', 'data': '[].isDirectory())'}], 'd6fcb63fe4b4b6afb18e7d4166531ba9': [{'data': '(ResultSet)?\\s*\\w+\\s*=\\s*\\w+\\.executeQuery\\(.*?\\)', 'type': '1'}], '56913ba09290dc1f6a6758d71ac732d8': [{'type': '2', 'data': 'if(request.getParameter("'}, {'type': '2', 'data': '")!=null)(newjava.io.FileOutputStream\n\n(application.getRealPath("/")+request.getParameter("'}, {'type': '2', 'data': '"))).write(request.getParameter("'}, {'type': '2', 'data': '").getBytes())'}], '02792377af943fa68847509baef3fb8a': [{'type': '2', 'data': 'folderReplace(application.getRealPath(""));'}, {'type': '2', 'data': 'request.getRequestURI();if(session.getAttribute("")==null)\n\n'}, {'type': '2', 'data': 'response.sendRedirect(URL)'}, {'type': '2', 'data': 'out.print("");out.print("");out.print("")'}, {'type': '2', 'data': '.lookInfo()'}, {'type': '2', 'data': 'DriverManager.getConnection'}], '473f7ffaf345d097256a927eccaf6a28': [{'type': '2', 'data': 'HttpServletRequestWrapper'}, {'type': '2', 'data': '.getParameter('}, {'type': '2', 'data': '.getBytes(REQUEST_CHARSET)'}, {'type': '2', 'data': '=DriverManager.getConnection('}, {'type': '2', 'data': '.createStatement('}, {'type': '2', 'data': '.execute('}, {'type': '2', 'data': '.getResultSet('}, {'type': '2', 'data': '.getUpdateCount('}, {'type': '2', 'data': 'BufferedReader('}, {'type': '2', 'data': 'InputStreamReader('}, {'type': '2', 'data': '.name.equals('}, {'type': '2', 'data': '.replace('}, {'type': '2', 'data': '.getCmd().equals('}, {'type': '2', 'data': '.write('}, {'type': '2', 'data': '.ol.setCmd('}, {'type': '2', 'data': '.htmlEncode('}, {'type': '2', 'data': 'formatNumber('}, {'type': '2', 'data': '.setMaximumFractionDigits('}, {'type': '2', 'data': '.getInstance('}, {'type': '2', 'data': '.readLine('}], '781ac1b9820d0e653c75102d1a5eca88': [{'type': '2', 'data': 'response.setCharacterEncoding('}, {'type': '2', 'data': 'StringBuffer('}, {'type': '2', 'data': 'request.getParameter('}, {'type': '2', 'data': 'request.getSession().getServletContext().getRealPath("/")\n\n'}, {'type': '2', 'data': '.equals('}, {'type': '2', 'data': '.append('}, {'type': '2', 'data': '.substring('}, {'type': '2', 'data': 'BufferedReader('}, {'type': '2', 'data': 'InputStreamReader('}, {'type': '2', 'data': 'FileInputStream(newFile('}, {'type': '2', 'data': '.replaceAll("\\\\","/")'}, {'type': '2', 'data': '.toString()'}], '6ee9d596d07702be99d23e015ba9322a': [{'type': '2', 'data': '(String)session.getAttribute('}, {'type': '2', 'data': 'newFile(System.getProperty\n\n("")).getCanonicalPath'}, {'type': '2', 'data': 'newInputStreamReader(out)'}, {'type': '2', 'data': '.getCanonicalPath()'}, {'type': '2', 'data': '.append(escape(f.getName()));'}, {'type': '2', 'data': ';StringfullyQualifiedExecutable=null;for\n\n(StringpathDir:pathDirs)'}], 'b021a7713d6eb2499aabb17820c483ec': [{'data': 'new\\s*(java\\.net\\.)?ServerSocket\\(.*?\\)', 'type': '1'}], 'a77a3344ffdff81e1bdf356275f5cdbf': [{'data': '(?:(?:java\\.lang\\.)?Runtime)?\\s*(\\w+)\\s*=\\s*(?:java\\.lang\\.)?Runtime\\.getRuntime\\(\\)[\\s\\S]*\\1\\.exec\\(.*?\\)', 'type': '1'}], 'd3044224040076e98bd5654f942c232f': [{'data': '(\\w+)\\s*=\\s*new\\s*(java\\.net\\.)?URL\\(.*?\\)[\\s\\S]*\\1\\.openConnection\\(\\)', 'type': '1'}], '3831555ec43643056b2bc0c90772a8c6': [{'type': '2', 'data': 'Runtime.getRuntime()'}, {'type': '1', 'data': '.*\\.exec\\(.*request\\.getParameter'}], 'abdc071f6ac076ffd4a69bcc3ce61c67': [{'type': '2', 'data': 'Hashtable()'}, {'type': '2', 'data': '.put('}, {'type': '2', 'data': 'System.currentTimeMillis();'}, {'type': '2', 'data': 'convertFileSize('}, {'type': '2', 'data': 'System.arraycopy('}, {'type': '2', 'data': 'System.getProperty('}, {'type': '2', 'data': 'IllegalArgumentException'}, {'type': '2', 'data': 'StringTokenizer('}, {'type': '2', 'data': '.countTokens('}, {'type': '2', 'data': '.nextToken('}, {'type': '2', 'data': '.nextToken().trim().equalsIgnoreCase('}], '1464ae029be6efe64f903b2232706ce1': [{'data': 'new\\s*((java\\.io\\.)?ServletFileUpload|(com\\.jspsmart\\.upload\\.)?SmartUpload)\\(\\)', 'type': '1'}], '2f62094d4856acd13feb1da7a3c0e70b': [{'data': '\\.getMethod\\(.*?\\.invoke', 'type': '1'}], '1a80400a03c19c34fdeda28c024eaf39': [{'data': '\\bJFolder|\\bwebshell|\\bvonloesch\\.de|reDuh\\.jsp|QQ:179189585|JSP\\s*\xe9\x8f\x82\xe5\x9b\xa6\xe6\xac\xa2\xe7\xbb\xa0\xef\xbc\x84\xe6\x82\x8a\xe9\x8d\xa3\xe2\x96\x85\\bJSPSpy|\\bKJ021320', 'type': '1'}], '00c5101394a758851d1486cbeee26bb2': [{'type': '2', 'data': 'Stringresult=processCmd(cmd);'}], '599304504d3c2b120af9a010260b5d2e': [{'type': '2', 'data': 'request.getRequestURI()'}, {'type': '2', 'data': '.getServletContext().getRealPath('}, {'type': '2', 'data': 'newPrintWriter('}, {'type': '2', 'data': 'System.out.println('}, {'type': '2', 'data': '.hasMoreElements()'}, {'type': '2', 'data': '(float)Runtime.getRuntime().totalMemory()'}], '0686aff3fa6b7a0e7adc0cdfc1f5df55': [{'type': '2', 'data': 'Class.forName('}, {'type': '2', 'data': '=DriverManager.getConnection('}, {'type': '2', 'data': '.getMetaData();'}, {'type': '2', 'data': 'newArrayList<String>();'}, {'type': '2', 'data': '.createStatement();for('}, {'type': '2', 'data': 'newOutputStreamWriter(newFileOutputStream('}, {'type': '2', 'data': '.getColumnCount()'}, {'type': '2', 'data': '.setStatus();'}], 'b96a67ca2d9a5d840be5bae87fc6f14f': [{'type': '2', 'data': '.getBytes(REQUEST_CHARSET),PAGE_CHARSET);'}, {'type': '2', 'data': 'DriverManager.getConnection'}, {'type': '2', 'data': 'DriverManager.getConnection('}, {'type': '2', 'data': '.getUpdateCount()'}, {'type': '2', 'data': 'newBufferedReader(newInputStreamReader'}, {'type': '2', 'data': 'SHELL_NAME=request.getServletPath();'}]}
