%define base_name	kwin-style
%define theme_name	mallory
%define name		%{base_name}-%{theme_name}
%define version		0.9
%define release %mkrel 7
%define summary		Mallory kwinstyle for KDE

Name:			%{name}
Version:		%{version}
Release:		%{release}
Summary:		%{summary}
License:		GPL
Group:			Graphical desktop/KDE
Source:			21650-%{theme_name}-%{version}.tar.bz2
Patch0:			mallory-0.9-automake.patch
URL:			http://kdelook.org/content/show.php?content=21650
BuildRequires:		kdebase-devel
BuildRequires:		chrpath

%description
Just another very flat window decoration with very original 
bouncing buttons. A few color schemes are provided too.

See README because this window decoration uses more colors 
than just title blend and title text colors.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{theme_name}-%{version}
%patch0 -p1 -b .automake

%build
make -f admin/Makefile.common cvs

export QTDIR=%_prefix/%_lib/qt3
export KDEDIR=%_prefix

export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

# Search for qt/kde libraries in the right directories (avoid patch)
# NOTE: please don't regenerate configure scripts below
perl -pi -e "s@/lib(\"|\b[^/])@/%_lib\1@g if /(kde|qt)_(libdirs|libraries)=/" configure

%{?__cputoolize: %{__cputoolize} }
%configure --disable-rpath

%make

%install
%makeinstall_std

cat > $RPM_BUILD_DIR/%{theme_name}-%{version}/README.urpmi << EOF

######################### More informations ########################

To use this win deco use kcontrol section apparence (LookNFeel)
and choose Mallory theme.


#######################################################################
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO INSTALL ChangeLog README.urpmi
%{_libdir}/kde3/kwin3_%{theme_name}*
%{_libdir}/kde3/kwin_%{theme_name}_config.*
%{_datadir}/apps/kwin/%{theme_name}.desktop
%{_datadir}/apps/kdisplay/color-schemes/Mallory.Camouflage.kcsrc
%{_datadir}/apps/kdisplay/color-schemes/Mallory.Double.Blue.kcsrc
%{_datadir}/apps/kdisplay/color-schemes/Mallory.Double.Grey.kcsrc
%{_datadir}/apps/kdisplay/color-schemes/Mallory.Flat.Blue.kcsrc
%{_datadir}/apps/kdisplay/color-schemes/Mallory.Flat.Grey.kcsrc
%{_datadir}/apps/kdisplay/color-schemes/Mallory.Flat.Sands.kcsrc
%{_datadir}/apps/kdisplay/color-schemes/Mallory.Forrest.kcsrc
%{_datadir}/apps/kdisplay/color-schemes/Mallory.Grey.and.Blue.kcsrc
%{_datadir}/apps/kdisplay/color-schemes/Mallory.Halo.Blue.kcsrc
%{_datadir}/apps/kdisplay/color-schemes/Mallory.Halo.Green.kcsrc
%{_datadir}/apps/kdisplay/color-schemes/Mallory.Sandy.kcsrc


