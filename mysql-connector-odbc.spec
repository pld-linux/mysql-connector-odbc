%define		_ver	22r857
Summary:	MySQL Connector/ODBC - ODBC driver for MySQL
Summary(pl.UTF-8):	MySQL Connector/ODBC - sterownik ODBC dla MySQL
Name:		mysql-connector-odbc
Version:	3.51
Release:	1
License:	GPL
Group:		Libraries
#Source0:	http://sunsite.icm.edu.pl/mysql/Downloads/MyODBC3/%{name}-%{version}.%{_ver}.tar.gz
Source0:	http://sunsite.informatik.rwth-aachen.de/mysql/Downloads/Connector-ODBC/3.51/%{name}-%{version}.%{_ver}.tar.gz
# Source0-md5:	0147e833711c9ef70c03f57c2641ef9f
URL:		http://www.mysql.com/products/connector/odbc/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	libiodbc-devel >= 3.0
BuildRequires:	qt-devel >= 1:3.0
#BuildRequires:	unixODBC-devel >= 3.0
BuildRequires:	unixODBC-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQL Connector/ODBC (also known as MyODBC) allows you to connect 
to a MySQL database server using the ODBC database API on all 
Microsoft Windows and most Unix platforms, including through 
such applications and programming environments such as 
Microsoft Access, Microsoft Excel, and Borland Delphi.

%description -l pl.UTF-8
MySQL Connector/ODB (znany także jako MyODBC) umożliwia połączenie
z serwerem MySQL przy wykorzystaniu API bazy ODBC na wszystkich
platformach Microsoft Windows oraz na większości systemów Unix,
włączając takie aplikacje i środowiska programistyczne jak
Microsoft Access, Microsoft Excel oraz Borland Delphi.

%prep
%setup -q -n %{name}-%{version}.%{_ver}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
LDFLAGS="%{rpmldflags} -L%{_libdir}"
%configure \
	--with-qt-includes=/usr/include/qt \
	--with-qt-libraries=%{_libdir}/qt \
	--with-x=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_datadir}/%{name}
