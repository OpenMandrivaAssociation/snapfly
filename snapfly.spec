Summary:	A lightweight PyGTK menu
Name:		snapfly
Version:	0.8
Release:	2
License:	GPLv3
Group:		Graphical desktop/Other
Url:		https://github.com/drakmail/snapfly
# from git
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	python-setuptools
BuildArch:	noarch
Requires:	pygtk2
Requires:	python-cairo
Requires:	python-dbus
Requires:	python-pyinotify

%description
SnapFly is a lightweight PyGTK menu which can be run as a daemon (in this
case you can call the menu from any place on your desktop using snapfly-show)
or as a standalone menu with a systray icon. The development began as a
patchset for adeskmenu, but nowadays SnapFly is almost fully rewritten.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%find_lang %{name} --with-man

%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/%{name}-show
%{python_sitelib}/%{name}
%{python_sitelib}/*.egg-info
%{_iconsdir}/hicolor/*/apps/%{name}.*
