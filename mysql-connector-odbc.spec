%define		_ver	12
Summary:	MySQL Connector/ODBC - ODBC driver for MySQL
Summary(pl):	MySQL Connector/ODBC - sterownik ODBC dla MySQL
Name:		mysql-connector-odbc
Version:	3.51
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://sunsite.icm.edu.pl/mysql/Downloads/MyODBC3/%{name}-%{version}.%{_ver}.tar.gz
# Source0-md5:	a484f590464fb823a8f821b2f1fd7fef
URL:		http://www.mysql.com/products/connector/odbc/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	libiodbc-devel >= 3.0
BuildRequires:	qt-devel >= 3.0
#BuildRequires:	unixODBC-devel >= 3.0
BuildRequires:	unixODBC-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQL Connector/ODBC (also known as MyODBC) allows you to connect 
to a MySQL database server using the ODBC database API on all 
Microsoft Windows and most Unix platforms, including through 
such applications and programming environments such as 
Microsoft Access, Microsoft Excel, and Borland Delphi.

%description -l pl
MySQL Connector/ODB (znany tak¿e jako MyODBC) umo¿liwia po³±czenie
z serwerem MySQL przy wykorzystaniu API bazy ODBC na wszystkich
platformach Microsoft Windows oraz na wiêkszo¶ci systemów Unix,
w³±czaj±c takie aplikacje i ¶rodowiska programistyczne jak
Microsoft Access, Microsoft Excel oraz Borland Delphi.

%prep
%setup -q -n %{name}-%{version}.%{_ver}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} \
	--with-x=no

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
