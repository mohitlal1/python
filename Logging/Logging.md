# Logging:
First of all, we need to import the logging module, followed by using the logger to check the current status and log messages. We are having 5 severity levels namely:
- Warning
- Info
- Error
- Critical
- Debug	
```sh		
		Code:
			Import logging
			logging.debug('a debug message')
			logging.info('an info message')
			logging.warning('a warning message')
			logging.error('an error message')
			logging.critical('a critical message')
```
```sh
		Output:
			WARNING:root: a warning message
			ERROR:root: an error message
			CRITICAL:root: a critical message
```
```sh
		Code:
			Import logging
			logging.basicConfig(filename='app.log', filemode='w',
			format='%(name)s - %(levelname)s - %(message)s')
			logging.warning('This gets logged to a file')
```
```sh
		Output:
			root - ERROR - This gets logged to a file
```
Here the file mode is said to write only so we have rights to rewrite the contents of the file. By default this configuration it opens in append mode only.	