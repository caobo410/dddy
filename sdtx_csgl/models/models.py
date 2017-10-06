# -*- coding: utf-8 -*-
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Odoo Connector
# QQ:61365857
# 邮件:caobo@shmingjiang.org.cn
# 手机：15562666538
# 作者：'caobo'
# 公司网址： www.goderp.com
# 山东开源ERP有限公司
# 日期：2015-12-18
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
import logging
from openerp import fields,models,api
from datetime import datetime
date_ref = datetime.now().strftime('%Y-%m-%d')
_logger = logging.getLogger(__name__)
class csgl_ggmk(models.Model):
    _name = "csgl.ggmk"
    _description = "csgl.ggmk"

    name = fields.Char(string='名称', size=64, required=True, help="名称")
    grade_typ = fields.Selection([('One', '一级'),
                                  ('Two', '二级')], 'Picture Type', required=True, help="模块等级")
    messages = fields.Char(string='备注', help="备注")
    user_id = fields.Many2one('res.users', string='制单人')
    date_confirm = fields.Date(string='制单日期', size=64, required=True, help="制单日期")
    _defaults = {
        'date_confirm': date_ref,
        'user_id': lambda cr, uid, id , c={}: id,
    }
class csgl_kfry(models.Model):
    _name = "csgl.kfry"
    _description = "csgl.kfry"

    name = fields.Char(string='姓名', size=64, required=True, help="姓名")
    messages = fields.Char(string='备注', help="备注")
    user_id = fields.Many2one('res.users', string='制单人')
    date_confirm = fields.Date(string='制单日期', size=64, required=True, help="制单日期")
    _defaults = {
        'date_confirm': date_ref,
        'user_id': lambda cr, uid, id, c={}: id,
    }
class csgl_bug(models.Model):
    _name = "csgl.bug"
    _description = "csgl.bug"

    name = fields.Char(string='名称', size=64, required=True, help="名称")

    ggmk_one_id = fields.Many2one('csgl.ggmk', string='一级模块', select=True)
    ggmk_two_id = fields.Many2one('csgl.ggmk', string='二级模块', select=True)
    kfry_id = fields.Many2one('csgl.kfry', string='开发人员', select=True)
    type = fields.Selection([('Nofixed', '未修复'),
                             ('Fixed', '已修复'),
                             ('BUGInvalid', '无效BUG'),
                             ('Noreproduce ', '无法重现')], '状态',default='Nofixed', required=True, help="类型")
    grade_typ = fields.Selection([('One', '一级'),
                                  ('Two', '二级'),
                                  ('Three', '三级')], '等级',default='Three', required=True, help="等级")
    messages = fields.Text(string='备注', help="备注")
    image = fields.Binary(string="image", help="图片大小建议 300x300px.")
    image_one = fields.Binary(string="image_one", help="图片大小建议 300x300px.")
    check_id = fields.Many2one('res.users', string='审核人')
    check_date = fields.Date(string='审核日期', size=64, help="审核日期")
    user_id = fields.Many2one('res.users', string='制单人')
    date_confirm = fields.Date(string='制单日期', size=64, required=True, help="制单日期")

    _defaults = {
        'date_confirm': date_ref,
        'user_id': lambda cr, uid, id, c={}: id,
    }


class yygl_gzrw(models.Model):
    _name = "yygl.gzrw"
    _description = "yygl.gzrw"

    name = fields.Char(string='名称', size=64, required=True, help="名称")

    ggmk_one_id = fields.Many2one('csgl.ggmk', string='一级模块', select=True)
    ggmk_two_id = fields.Many2one('csgl.ggmk', string='二级模块', select=True)
    kfry_id = fields.Many2one('csgl.kfry', string='开发人员', select=True)
    type = fields.Selection([('Nofixed', '未修复'),
                             ('Fixed', '已修复'),
                             ('BUGInvalid', '无效BUG'),
                             ('Noreproduce ', '无法重现')], '状态', default='Nofixed', required=True, help="类型")
    grade_typ = fields.Selection([('One', '一级'),
                                  ('Two', '二级'),
                                  ('Three', '三级')], '等级', default='Three', required=True, help="等级")
    messages = fields.Text(string='备注', help="备注")
    image = fields.Binary(string="image", help="图片大小建议 300x300px.")
    image_one = fields.Binary(string="image_one", help="图片大小建议 300x300px.")
    check_id = fields.Many2one('res.users', string='审核人')
    check_date = fields.Date(string='审核日期', size=64, help="审核日期")
    user_id = fields.Many2one('res.users', string='制单人')
    date_confirm = fields.Date(string='制单日期', size=64, required=True, help="制单日期")

    _defaults = {
        'date_confirm': date_ref,
        'user_id': lambda cr, uid, id, c={}: id,
    }

    # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: