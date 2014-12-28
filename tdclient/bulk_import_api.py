#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import with_statement

try:
    from urllib import quote as urlquote
except ImportError:
    from urllib.parse import quote as urlquote

class BulkImportAPI(object):
    ####
    ## Bulk import API
    ##

    # => nil
    def create_bulk_import(self, name, db, table, params={}):
        code, body, res = self.post("/v3/bulk_import/create/%s/%s/%s" % (urlquote(str(name)), urlquote(str(db)), urlquote(str(table))), params)
        if code != 200:
            self.raise_error("Create bulk import failed", res)
        end
        return None

    # => nil
    def delete_bulk_import(self, name, params={}):
        code, body, res = self.post("/v3/bulk_import/delete/%s" % (urlquote(str(name))), params)
        if code != 200:
            self.raise_error("Delete bulk import failed", res)
        end
        return None

    # => data:Hash
    def show_bulk_import(self, name):
        code, body, res = self.get("/v3/bulk_import/show/%s" % (urlquote(str(name))))
        if code != 200:
            self.raise_error("Show bulk import failed", res)
        end
        js = self.checked_json(body, ["status"])
        return js

    # => result:[data:Hash]
    def list_bulk_imports(self, params={}):
        code, body, res = self.get("/v3/bulk_import/list", params)
        if code != 200:
            self.raise_error("List bulk imports failed", res)
        js = self.checked_json(body, ["bulk_imports"])
        return js["bulk_imports"]

    def list_bulk_import_parts(self, name, params={}):
        code, body, res = self.get("/v3/bulk_import/list_parts/%s" % (urlquote(str(name))), params)
        if code != 200:
            self.raise_error("List bulk import parts failed", res)
        js = self.checked_json(body, ["parts"])
        return js["parts"]

    # => nil
    def bulk_import_upload_part(self, name, part_name, stream, size):
        code, body, res = self.put("/v3/bulk_import/upload_part/%s/%s" % (urlquote(str(name)), urlquote(str(part_name))), stream, size)
        if code / 100 != 2:
            self.raise_error("Upload a part failed", res)
        return None

    # => nil
    def bulk_import_delete_part(self, name, part_name, parms={}):
        code, body, res = self.post("/v3/bulk_import/delete_part/%s/%s" % (urlquote(str(name)), urlquote(str(part_name))), params)
        if code / 100 != 2:
            self.raise_error("Delete a part failed", res)
        return None

    # => nil
    def freeze_bulk_import(self, name, params={}):
        code, body, res = self.post("/v3/bulk_import/freeze/%s" % (urlquote(str(name))), params)
        if code != 200:
            self.raise_error("Freeze bulk import failed", res)
        return None

    # => nil
    def unfreeze_bulk_import(self, name, params={}):
        code, body, res = self.post("/v3/bulk_import/unfreeze/%s" % (urlquote(str(name))), params)
        if code != 200:
            self.raise_error("Unfreeze bulk import failed", res)
        return None

    # => jobId:String
    def perform_bulk_import(self, name, params={}):
        code, body, res = self.post("/v3/bulk_import/perform/%s" % (urlquote(str(name))), params)
        if code != 200:
            self.raise_error("Perform bulk import failed", res)
        js = self.checked_json(body, ["job_id"])
        return str(js["job_id"])

    # => nil
    def commit_bulk_import(self, name, params={}):
        code, body, res = self.post("/v3/bulk_import/commit/%s" % (urlquote(str(name))), params)
        if code != 200:
            eslf.raise_error("Commit bulk import failed", res)
        return None