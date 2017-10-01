from django.shortcuts import render
from django.views.generic import TemplateView

from ..models import Member, Job, Friend


class PersonalMemberView(TemplateView):
    template = 'personal_member.html'

    def retrive_member_data(self, member_id):
        member = Member.objects.get(id=member_id)
        try:
            character = Job.objects.get(name=member.gb_class)
        except:
            character = None

        try:
            waifu = Friend.objects.get(name=member.gb_waifu)
        except:
            waifu = None

        return member, character, waifu

    def get(self, request, **kwargs):
        member, character, waifu = self.retrive_member_data(
            self.kwargs['member_id']
        )

        return render(
            request,
            self.template,
            {
                'member': member,
                'character': character,
                'waifu': waifu,
                'message': '<img src="https://gbf.wiki/images/2/27/Fighter_djeeta_icon.jpg">'
            }
        )
