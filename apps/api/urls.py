# @Author  : cheertt
# @Time    : 2019/3/6 8:46
# @Remark  : api界面的相关url链接
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from api import views_member, views_credit
from api import views_commodity
from api import views_recommendations
from api import views_hotcommend
urlpatterns = [
    # 会员信息增改删查操作
    url(r'^member/$', views_member.MemberView.as_view(), name="member"),
    url(r'^member/savepic', views_member.MemberUploadFace.as_view(), name="member-save-face"),
    url(r'^member/login', csrf_exempt(views_member.MemberLoginView.as_view()), name="member-login"),
    url(r'^member/checkreg', csrf_exempt(views_member.MemberCheckRegView.as_view()), name="member-checkreg"),
    url(r'^member/info', views_member.MemberInfoView.as_view(), name="member-info"),
    url(r'^member/order', views_member.MemberOrderView.as_view(), name='member-order'),
    url(r'^member/credit_list', views_credit.CreditListView.as_view(), name='credit-list'),
    url(r'^member/credit_share', csrf_exempt(views_credit.ShareView.as_view()), name='credit-share'),

    url(r'^commodity/comment_add', views_commodity.CommentAddView.as_view(), name='comment-add'),
    url(r'^commodity/search', views_commodity.CommoditySearchView.as_view(), name="commodity-search"),
    url(r'^commodity/commodity_type', views_commodity.CommodityTypeView.as_view(), name="commodity-type"),
    url(r'^commodity/commodity_list', views_commodity.CommodityListView.as_view(), name="commodity-list"),
    url(r'^commodity/commodity_info', views_commodity.CommodityInfoView.as_view(), name="commodity-info"),
    url(r'^commodity/commodity_comments', views_commodity.CommodityCommentsView.as_view(), name="commodity-comments"),
    url(r'^commodity/cart_add', views_commodity.CartAddView.as_view(), name="cart-add"),
    url(r'^commodity/cart_list', views_commodity.CartListView.as_view(), name="cart-list"),
    url(r'^commodity/cart_del', csrf_exempt(views_commodity.CartDeltView.as_view()), name="cart-del"),

    url(r'^recommendations/toprecommendations', csrf_exempt(views_recommendations.TopRecommendationsView.as_view()), name="TopRecommendations"),
    url(r'^recommendations/allrecommendations', csrf_exempt(views_recommendations.AllRecommendationsView.as_view()),
        name="AllRecommendations"),
    url(r'^recommendations/commonrecommendations',csrf_exempt(views_recommendations.Get_Common_Recommenadations.as_view()), name="CommonRecommendations"),
    url(r'^hotcommend/hot_commodity', views_hotcommend.HotCommodityView.as_view(), name="hot-commodity"),


]