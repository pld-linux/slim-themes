Summary:	Themes for SLiM
Summary(pl.UTF-8):	Motywy dla SLiM
Name:		slim-themes
Version:	1.2.3
Release:	1
License:	GPL
Group:		Themes
Source0:	http://download.berlios.de/slim/slim-%{version}-themepack1a.tar.gz
# Source0-md5:	fd1295d3a260849790dc17081da4a34f
URL:		http://download.berlios.de/slim/
Requires:	slim-theme-capernoited
Requires:	slim-theme-flower2
Requires:	slim-theme-isolated
Requires:	slim-theme-lotus-midnight
Requires:	slim-theme-lotus-sage
Requires:	slim-theme-mindlock
Requires:	slim-theme-parallel-dimensions
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a set of themes for SLiM display manager
(metapackage).

%description -l pl.UTF-8
Ten pakiet dostarcza zestaw motywów do zmiany wyglądu zarządcy ekranów
SLiM (metapakiet).

%package -n slim-theme-capernoited
Summary:	Theme capernoited for SLiM
Summary(pl.UTF-8):	Motyw capernoited dla SLiM
Group:		Themes
Requires:	slim

%description -n slim-theme-capernoited
This package provdes `capernoited' theme for SLiM display manager.

%description -n slim-theme-capernoited -l pl.UTF-8
Pakiet ten dostarcza motywu `capernoited' do zarządcy ekranow SLiM.

%package -n slim-theme-flower2
Summary:	Theme flower2 for SLiM
Summary(pl.UTF-8):	Motyw flower2 dla SLiM
Group:		Themes
Requires:	slim

%description -n slim-theme-flower2
This package provdes `flower2' theme for SLiM display manager.

%description -n slim-theme-flower2 -l pl.UTF-8
Pakiet ten dostarcza motywu `flower2' do zarządcy ekranow SLiM.

%package -n slim-theme-isolated
Summary:	Theme isolated for SLiM
Summary(pl.UTF-8):	Motyw isolated dla SLiM
Group:		Themes
Requires:	slim

%description -n slim-theme-isolated
This package provdes `isolated' theme for SLiM display manager.

%description -n slim-theme-isolated -l pl.UTF-8
Pakiet ten dostarcza motywu `isolated' do zarządcy ekranow SLiM.

%package -n slim-theme-lotus-midnight
Summary:	Theme lotus-midnight for SLiM
Summary(pl.UTF-8):	Motyw lotus-midnight dla SLiM
Group:		Themes
Requires:	slim

%description -n slim-theme-lotus-midnight
This package provdes `lotus-midnight' theme for SLiM display manager.

%description -n slim-theme-lotus-midnight -l pl.UTF-8
Pakiet ten dostarcza motywu `lotus-midnight' do zarządcy ekranow SLiM.

%package -n slim-theme-lotus-sage
Summary:	Theme lotus-sage for SLiM
Summary(pl.UTF-8):	Motyw lotus-sage dla SLiM
Group:		Themes
Requires:	slim

%description -n slim-theme-lotus-sage
This package provdes `lotus-sage' theme for SLiM display manager.

%description -n slim-theme-lotus-sage -l pl.UTF-8
Pakiet ten dostarcza motywu `lotus-sage' do zarządcy ekranow SLiM.

%package -n slim-theme-mindlock
Summary:	Theme mindlock for SLiM
Summary(pl.UTF-8):	Motyw mindlock dla SLiM
Group:		Themes
Requires:	slim

%description -n slim-theme-mindlock
This package provdes `mindlock' theme for SLiM display manager.

%description -n slim-theme-mindlock -l pl.UTF-8
Pakiet ten dostarcza motywu `mindlock' do zarządcy ekranow SLiM.

%package -n slim-theme-parallel-dimensions
Summary:	Theme parallel-dimensions for SLiM
Summary(pl.UTF-8):	Motyw parallel-dimensions dla SLiM
Group:		Themes
Requires:	slim

%description -n slim-theme-parallel-dimensions
This package provdes `parallel-dimensions' theme for SLiM display
manager.

%description -n slim-theme-parallel-dimensions -l pl.UTF-8
Pakiet ten dostarcza motywu `parallel-dimensions' do zarządcy ekranow
SLiM.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

for i in capernoited flower2 isolated lotus-midnight lotus-sage mindlock parallel-dimensions;
do
	install -d $RPM_BUILD_ROOT%{_datadir}/slim/themes/$i
	install $i/{background.jpg,panel.png,slim.theme} \
		$RPM_BUILD_ROOT%{_datadir}/slim/themes/$i
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files -n slim-theme-capernoited
%defattr(644,root,root,755)
%doc capernoited/README
%{_datadir}/slim/themes/capernoited

%files -n slim-theme-flower2
%defattr(644,root,root,755)
%doc flower2/README
%{_datadir}/slim/themes/flower2

%files -n slim-theme-isolated
%defattr(644,root,root,755)
%doc isolated/README
%{_datadir}/slim/themes/isolated

%files -n slim-theme-lotus-midnight
%defattr(644,root,root,755)
%doc lotus-midnight/{README,LICENSE.panel,COPYRIGHT.panel}
%{_datadir}/slim/themes/lotus-midnight

%files -n slim-theme-lotus-sage
%defattr(644,root,root,755)
%doc lotus-sage/{README,LICENSE.panel,COPYRIGHT.panel}
%{_datadir}/slim/themes/lotus-sage

%files -n slim-theme-mindlock
%defattr(644,root,root,755)
%doc mindlock/README
%{_datadir}/slim/themes/mindlock

%files -n slim-theme-parallel-dimensions
%defattr(644,root,root,755)
%doc parallel-dimensions/{LICENSE.panel,COPYRIGHT.{background,panel}}
%{_datadir}/slim/themes/parallel-dimensions
