Summary:	LatencyTOP: measuring and fixing Linux latency
Name:		latencytop
Version:	0.5
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://www.latencytop.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	73bb3371c6ee0b0e68e25289027e865c
Patch0:		%{name}-make.patch
URL:		http://www.latencytop.org/
BuildRequires:	glib2-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LatencyTOP is a Linux tool for software developers (both kernel and
userspace), aimed at identifying where in the system latency is
happening, and what kind of operation/action is causing the latency to
happen so that the code can be changed to avoid the worst latency
hiccups.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a latencytop.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/latencytop
%{_mandir}/man8/latencytop.8*
%{_datadir}/latencytop
