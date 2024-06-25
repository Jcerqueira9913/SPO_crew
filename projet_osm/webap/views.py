from django.shortcuts import render

# Create your views here.
from bs4 import BeautifulSoup

def extrair_dados_html(html, tag, atributo=None, valor_atributo=None):
    # Analisa o HTML com BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Procura a tag e os atributos desejados
    if atributo and valor_atributo:
        elementos = soup.find_all(tag, {atributo: valor_atributo})
    else:
        elementos = soup.find_all(tag)

    # Extrai o texto dos elementos encontrados
    dados = [elemento.text for elemento in elementos]

    return dados

# Exemplo de uso
html = '''
<table id="crew-member-table" class="table table-sticky thSortable">
                                                <thead>
                                                    <tr class="thead">
                                                        <th class="text-left th-manager-width" data-bind="click: orderByUserName">Manager</th>
                                                        <th class="text-center th-icon-width th-unsortable">Chat</th>
                                                            <th class="text-left th-rank-width" data-bind="click: orderByBattleForm">Battle points</th>
                                                        <th class="text-center th-icon-width" data-bind="click: orderByNationality">Nationality</th>
                                                        <th class="text-left th-login-width" data-bind="click: orderByLastLogin">Last seen</th>
                                                        <th class="text-center th-icon-width" data-bind="click: orderByStatus">Hierarchy</th>
<!-- ko if: isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                    </tr>
                                                </thead>
                                                <tbody>
<!-- ko foreach: getItems -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="//osm.cloud/Images/Shared/default_userAvatar.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">n.jorge</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">1888</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">30 June</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon silver" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Davide da Silva Costa</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">1461</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">15:13</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">tbc111</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">1446</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">13:30</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon silver" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/31.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Mtx9900</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">1346</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">16:59</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon silver" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Tiago.21</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">1193</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">17 August</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon silver" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">hilarioSilva</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">1158</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">14:59</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon silver" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/129.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">nunobarbosa86</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">1157</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">11:10</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon silver" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">JNPires</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">1155</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">7 October</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">rafaelraf665</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">1077</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">16:24</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Paulinho Terror1906</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">745</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">17:16</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Pepe_31</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">692</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">16:55</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">perfilariam</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">688</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">7 October</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Defected66</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">655</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">16:59</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">EmanuelJLC</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">594</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">09:53</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/34.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Guitta76</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">546</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">15:58</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon gold" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">FaCarreira</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">496</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-ca" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="CA"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">06:49</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="//osm.cloud/Images/Shared/default_userAvatar.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">PutoFananBoy</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">439</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">27 September</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Champion38866</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">407</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">6 June</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/138.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Davide Oliveira 89</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">401</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">09:36</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/138.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">PinOkaS</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">215</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">12:27</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/3.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">sequeira5</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">206</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">7 October</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">TiburcioFC</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">155</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">7 October</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/12.jpg?v=3.188.5">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Cláudia Inês</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">148</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">14:02</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon silver" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) --><!-- /ko --><!-- /ko -->                                                    <!-- ko if: $root.crewPartial().isUserMemberOfCrew(appViewModel.userPartial().id) --><!-- /ko -->                                                </tbody>
                                            </table>
'''

tag = 'span'
atributo = 'class'
valor_atributo = 'semi-bold'


def remove(ocor,a):
    while ocor in a:
        a.remove(ocor)
    return a

resultado =remove("\n\n",extrair_dados_html(html, tag, atributo, valor_atributo))

pnt=resultado[1::3]

while '-' in pnt:
    pnt.remove('-')

while len(pnt)<24:
    pnt.append('0')

name=resultado[::3]

while len(name)<24:
    name.append('')

dic_pnt=dict()
for i,j in zip(pnt,name):
    dic_pnt[j]=i
print(dic_pnt)
pnts={'n.jorge': '1888', 'Davide da Silva Costa': '1461', 'tbc111': '1446', 'Mtx9900': '1346', 'Tiago.21': '1193', 'hilarioSilva': '1158', 'nunobarbosa86': '1157', 'JNPires': '1155', 'rafaelraf665': '1077', 'Paulinho Terror1906': '745', 'Pepe_31': '692', 'perfilariam': '688', 'Defected66': '655', 'EmanuelJLC': '594', 'Guitta76': '546', 'FaCarreira': '496', 'PutoFananBoy': '439', 'Champion38866': '407', 'Davide Oliveira 89': '401', 'PinOkaS': '215', 'sequeira5': '206', 'TiburcioFC': '155', 'Cláudia Inês': '148', '': '0'}
pts=[]
for k in name:
    pts.append((int(dic_pnt[k]))-(int(pnts[k])))

order=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

dic=dict()
for h,k,l in zip(order,pts,name):
    dic[h] = [l,k,'not available yet','Oct 8 18h11']

sorted_items = sorted(dic.items(), key=lambda x: x[1][1], reverse=True)
dic = {i + 1: item for i, (key, item) in enumerate(sorted_items)}

data_1=dic.get(1, [])
data_2=dic.get(2, [])
data_3=dic.get(3, [])
data_4=dic.get(4, [])
data_5=dic.get(5, [])
data_6=dic.get(6, [])
data_7=dic.get(7, [])
data_8=dic.get(8, [])
data_9=dic.get(9, [])
data_10=dic.get(10, [])
data_11=dic.get(11, [])
data_12=dic.get(12, [])
data_13=dic.get(13, [])
data_14=dic.get(14, [])
data_15=dic.get(15, [])
data_16=dic.get(16, [])
data_17=dic.get(17, [])
data_18=dic.get(18, [])
data_19=dic.get(19, [])
data_20=dic.get(20, [])
data_21=dic.get(21, [])
data_22=dic.get(22, [])
data_23=dic.get(23, [])
data_24=dic.get(24, [])

def index(request):
	return render(request, "webap/index.html", {"data_1": data_1, "data_2": data_2, "data_3": data_3, "data_4": data_4, "data_5": data_5, "data_6": data_6, "data_7": data_7, "data_8": data_8, "data_9": data_9, "data_10": data_10, "data_11": data_11, "data_12": data_12, "data_13": data_13, "data_14": data_14, "data_15": data_15, "data_16": data_16, "data_17": data_17, "data_18": data_18, "data_19": data_19, "data_20": data_20, "data_21": data_21, "data_22": data_22, "data_23": data_23, "data_24": data_24})
# Create your views here.