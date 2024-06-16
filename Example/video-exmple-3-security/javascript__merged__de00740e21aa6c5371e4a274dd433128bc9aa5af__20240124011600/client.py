"""
knox - Client
Copyright(c) 2010 LearnBoost <dev@learnboost.com>
MIT Licensed
"""
import utils
import auth
import http
import https
import url
import mime
import fs
import crypto
# The max for multi-object delete, bucket listings, etc.
BUCKET_OPS_MAX = 1000
def registerReqListeners(req, fn):
    req.on('response', lambda res: fn(None, res))
    req.on('error', fn)
def ensureLeadingSlash(filename):
    return '/' + filename if filename[0] != '/' else filename
class Client:
    def __init__(self, options):
        if 'key' not in options:
            raise ValueError('aws "key" required')
        if 'secret' not in options:
            raise ValueError('aws "secret" required')
        if 'bucket' not in options:
            raise ValueError('aws "bucket" required')
        if options['bucket'] != options['bucket'].lower():
            raise ValueError('AWS bucket names must be all lower case.')
        self.endpoint = options['bucket'] + '.s3.amazonaws.com'
        self.secure = True
        utils.merge(self, options)
        self.url = self.https if self.secure else self.http
    def request(self, method, filename, headers=None):
        options = {'host': self.endpoint}
        date = utils.Date()
        headers = headers or {}
        filename = ensureLeadingSlash(filename)
        # Default headers
        utils.merge(headers, {
            'Date': date.toUTCString(),
            'Host': self.endpoint
        })
        # Authorization header
        headers['Authorization'] = auth.authorization({
            'key': self.key,
            'secret': self.secret,
            'verb': method,
            'date': date,
            'resource': auth.canonicalizeResource('/' + self.bucket + filename),
            'contentType': headers['Content-Type'],
            'md5': headers['Content-MD5'] or '',
            'amazonHeaders': auth.canonicalizeHeaders(headers)
        })
        # Issue request
        options['method'] = method
        options['path'] = filename
        options['headers'] = headers
        req = (https if self.secure else http).request(options)
        req.url = self.url(filename)
        return req
    def put(self, filename, headers=None):
        headers = utils.merge({
            'Expect': '100-continue',
            'x-amz-acl': 'public-read'
        }, headers or {})
        return self.request('PUT', filename, headers)
    def putFile(self, src, filename, headers=None, fn=None):
        if callable(headers):
            fn = headers
            headers = {}
        stat = fs.stat(src)
        headers = utils.merge({
            'Content-Length': stat.size,
            'Content-Type': mime.lookup(src)
        }, headers)
        fileStream = fs.createReadStream(src)
        self.putStream(fileStream, filename, headers, fn)
    def putStream(self, stream, filename, headers=None, fn=None):
        req = self.put(filename, headers)
        registerReqListeners(req, fn)
        stream.on('error', fn)
        stream.pipe(req)
    def copyFiles(self, sourceFilename, destFilename, headers=None):
        headers = headers or {}
        # Copy files logic here
# Instantiate the Client class
client = Client({
    'key': 'your_aws_key',
    'secret': 'your_aws_secret',
    'bucket': 'your_bucket_name'
})
# Example usage
fs.stat('Readme.md', lambda err, stat: 
    client.putFile('Readme.md', '/test/Readme.md', {
        'Content-Length': stat.size,
        'Content-Type': 'text/plain'
    }, lambda err, res: 
        print(res.statusCode)
        print(res.headers)
    )
)