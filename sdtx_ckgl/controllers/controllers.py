# -*- coding: utf-8 -*-
from openerp import http, fields,api
import rest
import authorizer
from datetime import datetime

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO


date_ref = datetime.now().strftime('%Y-%m-%d')
# _logger = logging.getLogger(__name__)

class OrderController(http.Controller):
    @authorizer.authorize
    @http.route('/api/sdtx_ckgl/<database>', type='http', auth='none', methods=['POST'])
    def sdtx_ckgl(self, database, login, password, type, warehouse_list, line_list):
        if type:
            if type == u'xsck':
                name = u'销售出库单'
                print_name = u'sdtx_ckgl_report.report_sdtx_xsck_main'
            elif type == u'xsth':
                name = u'销售退货单'
                print_name = u'sdtx_ckgl_report.report_sdtx_xsth_main'
            elif type == u'cgrk':
                name = u'采购入库单'
                print_name = u'sdtx_ckgl_report.report_sdtx_cgrk_main'
            elif type == u'cgth':
                name = u'采购退货单'
                print_name = u'sdtx_ckgl_report.report_sdtx_cgth_main'
            elif type == u'dbd':
                name = u'调拨单'
                print_name = u'sdtx_ckgl_report.report_sdtx_dbd_main'
            elif type == u'qtck':
                name = u'其他出库单'
                print_name = u'sdtx_ckgl_report.report_sdtx_qtck_main'
            elif type == u'qtrk':
                name = u'其他入库单'
                print_name = u'sdtx_ckgl_report.report_sdtx_qtrk_main'
            else:
                return rest.render_json({'status': 'no', 'message': 'type类型不正确！'})
        else:
            return rest.render_json({'status': 'no', 'message': 'type不能为空！'})
        if not warehouse_list:
            return rest.render_json({'status': 'no', 'message': name + u'不能为空！'})
        if not line_list:
            return rest.render_json({'status': 'no', 'message': name + u'商品明细不能为空！'})
        try:
            warehouse_values = eval(warehouse_list)
            line_values = eval(line_list)
        except:
            return rest.render_json({'status': 'no', 'message': 'warehouse_values/line_values参数有问题！'})
        self.current_env.cr.execute('delete from ckgl_dddy;delete from dddy_line')
        sdtx_ckgl_obj = self.current_env['ckgl.dddy']
        sdtx_ckgl_line_obj = self.current_env['dddy.line']
        for warehouse_value in warehouse_values:
            sdtx_ckgl_obj.create(warehouse_value)
        for line_value in line_values:
            ckgl_obj = sdtx_ckgl_obj.search([('default_id', '=', line_value['default_id'])])
            line_value['line_id'] = ckgl_obj.id
            sdtx_ckgl_line_obj.create(line_value)
        report_objs = self.current_env['report']
        ckgl_objs = sdtx_ckgl_obj.search([])
        values = report_objs.get_pdf(ckgl_objs, print_name)
        return rest.render_pdf(values, type)
