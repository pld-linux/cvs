Summary:	Concurrent Versioning System
Summary(de):	Concurrent-Versioning-System
Summary(es):	Control de versiones en modo concurrente
Summary(fr):	Un syst�me pour maintenir � jour des fichiers
Summary(pl):	Concurrent Versioning System
Summary(pt_BR):	Controle de vers�es em modo concorrente
Summary(ru):	������� ���������� ��������
Summary(tr):	S�r�m denetim sistemi
Summary(uk):	������� ��������� ���Ӧ���
Summary(zh_CN):	�����İ汾����ϵͳCVS
Name:		cvs
Version:	1.11.5
Release:	1
License:	GPL
Group:		Development/Version Control
# active ftp only(?)
Source0:	http://ftp.cvshome.org/files/19/10/%{name}-%{version}.tar.bz2
Source1:	%{name}.inetd
Patch0:		%{name}-tmprace.patch
Patch1:		%{name}-info.patch
Patch2:		http://www.t17.ds.pwr.wroc.pl/~misiek/ipv6/%{name}-1.11.2-20020513-ipv6.patch.gz
Patch3:		%{name}-zlib.patch
Patch4:		%{name}-fixed_buffer.patch
Patch5:		%{name}-cvspass.patch
Patch6:		%{name}-home_etc.patch
Patch7:		%{name}-newnline.patch
Patch8:		%{name}-no_libnsl.patch
URL:		http://www.cyclic.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	zlib-devel
Obsoletes:	cvs-nserver-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_cvs_root	/home/services/cvsroot

%description
CVS means Concurrent Version System; it is a version control system
which can record the history of your files (usually, but not always,
source code). CVS only stores the differences between versions,
instead of every version of every file you've ever created. CVS also
keeps a log of who, when and why changes occurred, among other
aspects.

CVS is very helpful for managing releases and controlling the
concurrent editing of source files among multiple authors. Instead of
providing version control for a collection of files in a single
directory, CVS provides version control for a hierarchical collection
of directories consisting of revision controlled files. These
directories and files can then be combined together to form a software
release.

%description -l de
CVS ist ein Frontend f�r das RCS(1)-Revisionskontrollsystem, das den
Begriff der Revisionskontrolle von einer Sammlung von Dateien in einem
einzelnen Verzeichnis auf eine ganze Hierarchie ausweitet, bestehend
aus revisionskontrollierten Dateien. Diese Verzeichnisse und Dateien
lassen sich zu einer Software-Release kombinieren. CVS bietet die
Funktionen, die zur Verwaltung von Software-Releases und zur
�berwachung der gleichzeitigen Bearbeitung von Quelldateien durch
mehrere Software- Entwickler notwendig sind.

%description -l es
CVS es un front end para el rcs(1) - revisi�n control system - que
extiende la noci�n de control de revisi�n de una colect�nea de archivo
en un �nico directorio para una colecci�n jer�rquica de directorios
que contiene archivos controlados por revisi�n. Estos directorios y
archivos pueden ser combinados juntos para crear una release de
software. CVS nos ofrece las funciones necesarias para administrar
esta release de software y para controlar la edici�n concurrente de
archivos fuente por m�ltiples programadores.

%description -l fr
"CVS" signifie "Concurrent Version System". C'est un syst�me de
comparaison de versions de fichiers, qui peut garder une trace des
changements apport�s � des fichiers (le plus souvent, les fichiers des
sources d'un programme). CVS conserve seulement les diff�rences, et
non l'int�gralit� d'un fichier r�cent et d'un fichier plus ancien. A
chaque modification d'un fichier, CVS garde (entre autres) le nom de
la personne ayant fait la modification, la raison justifiant cette
modification, et la date � laquelle celle-ci a eu lieu.

CVS est tr�s utile pour g�rer la mise en commun des modifications
apport�es par plusieurs personnes travaillant en parall�le sur les
m�mes fichiers. Au lieu de garder plusieurs versions des fichiers dans
un seul r�pertoire, CVS cr�e une s�rie de r�pertoires, chacun
contenant une nouvelle version des fichiers. Ces r�pertoires et ces
fichiers peuvent ensuite �tre regroup�s pour former la version la plus
� jour du logiciel. Installez ce package si vous avez besoin
d'utiliser un syst�me de contr�le de version.

%description -l pl
CVS jest nak�adk� na rcs (Revision Control System, czyli w wolnym
t�umaczeniu system kontroli wersji zasob�w), kt�ry rozszerza
mo�liwo�ci rcs'a z narz�dzia do kontroli zbioru plik�w w pojedynczym
katalogu o mo�liwo�� kontroli zbioru hierarchicznie u�o�onych
katalog�w z plikami. Z pomoc� CVS w �atwy spos�b mo�na zarz�dza� kodem
�r�d�owym opracowywanym przez nawet bardzo du�e zespo�y programist�w
umo�liwiaj�c �ledzenie i kontrol� wszystkich zmian w trakcie pracy nad
projektami i wypuszczaniem pe�nych wersji oprogramowania (release).

%description -l pt_BR
CVS � um front end para o rcs(1) - revision control system - que
estende a no��o de controle de revis�o de uma colet�nea de arquivo em
um �nico diret�rio para uma cole��o hier�rquica de diret�rios que
cont�m arquivos controlados por revis�o. Esses diret�rios e arquivos
podem ser combinados juntos para criar uma release de software. CVS
oferece as fun��es necess�rias para administrar essas release de
software e para controlar a edi��o concorrente de arquivos fonte por
m�ltiplos programadores.

%description -l ru
CVS (Concurrent Version System) - ��� ������� ���������� ��������,
������� ����� �������� ������� ����� ������ (������, �� �� ������, ���
�������� ������). CVS ��������� ������ �������� ����� �������� ������
������ ������ ������� �����, ������� ���� �����-���� �������. �����
CVS ������ �������� ����, ���, ����� � ����� ���-���� �������.

CVS ����� ������� ��� ����������� ������� � ���������� ������������
������� �������� ������ ����������� ��������. ������ ��������������
���������� �������� ������ ������ � ����� �������� CVS �������������
���������� �������� �������������� ������ ���������, ��������� ��
������, �������� ������� ���� ����������. ��� ����� � �������� �����
���� ������� ������ ��� ������������ ������ ��.

%description -l tr
CVS (Concurrent Versioning System), tek bir dizindeki dosya
toplulu�unun s�r�m denetimini, denetimi yap�lm�� dizinlerin hiyerar�ik
toplulu�una geni�leten rcs(1) s�r�m denetim sisteminin �n y�z�d�r. Bu
dizin ve dosyalar, bir yaz�l�m yay�n� olu�turma amac�yla biraraya
getirilebilir. CVS, bu yaz�l�m yay�nlar�n�n y�netilmesini ve kaynak
dosyalar� bak�m�n�n birden �ok yaz�l�m geli�tiricisi taraf�ndan
e�zamanl� olarak yap�lmas�n� kontrol etmek i�in gereken i�levleri
sa�lar.

%description -l uk
CVS (Concurrent Version System) - �� ������� ��������� ���Ӧ���, ���
�ͦ� �������� ����Ҧ� ����� ���̦� (��������, ��� �� ������, ��
��Ȧ�Φ ������). CVS ���Ҧ��� Ԧ���� Ҧ����� ͦ� ���Ӧ��� ��ͦ���
����ϧ ���Ӧ� ������� �����, ��� ���� ������ ��������. ����� CVS
���Ҧ��� �������� ����, ���, ���� � ��צ�� ���� �ͦ���.

CVS ���� ������� ��� ����Φ��æ� ��̦ڦ� �� ��������� �����������
������� ��ڦ���� ���̦� ˦������ ��������. ��ͦ��� ������� ��������Ԧ
��������� ���Ӧ��� ������ ���̦� � ������ ������ڦ, CVS �����
�����צ��� ��������� �����Ȧ���� ������� ������Ǧ�, �� ����������� �
���̦�, ���Ӧ��� ������ ����� ��������. � ����� �� �������� ������
���� ڦ���Φ ����� ��� ���������� ��̦�� ��.

%package pserver
Summary:	rc-inetd config files to run CVS pserver
Summary(pl):	Pliki konfiguracyjne rc-ineta do postawienia pservera CVS
Group:		Development/Version Control
PreReq:		%{name} = %{version}
Requires:	rc-inetd
Obsoletes:	cvs-nserver-common
Obsoletes:	cvs-nserver-nserver
Obsoletes:	cvs-nserver-pserver

%description pserver
Config files for rc-inetd that are necessary to run CVS in pserver
mode.

%description pserver -l pl
Pliki konfiguracyjne rc-inetd niezb�dne do uruchomienia CVSa w trybie
pserver.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-server \
	--enable-client
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/sysconfig/rc-inetd,%{_cvs_root}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/cvs

rm -f contrib/{.cvsignore,Makefile*,*.pl,*.sh,*.csh}
mv -f $RPM_BUILD_ROOT%{_datadir}/cvs/contrib/rcs2log $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%pre pserver
if [ "$1" = 1 ]; then
	# Add user and group
	getgid cvs >/dev/null 2>&1 || %{_sbindir}/groupadd -f -g 52 cvs
	id -u cvs >/dev/null 2>&1 || %{_sbindir}/useradd -g cvs -d %{_cvs_root} -u 52 -s /bin/false cvs 2>/dev/null
fi

%post pserver
if [ "$1" = 1 ]; then
	# Initialise repository
	%{_bindir}/cvs -d :local:%{_cvs_root} init
	chown -R cvs.cvs %{_cvs_root}/CVSROOT
fi
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%postun pserver
if [ "$1" = "0" ]; then
	# Remove user and group
	%{_sbindir}/userdel cvs 2>/dev/null
	%{_sbindir}/groupdel cvs 2>/dev/null
	if [ -f /var/lock/subsys/rc-inetd ]; then
		/etc/rc.d/init.d/rc-inetd reload
	fi
fi

%files
%defattr(644,root,root,755)
%doc BUGS FAQ MINOR-BUGS NEWS PROJECTS TODO README ChangeLog doc/*.ps contrib
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[158]/*
%{_infodir}/cvs*

%files pserver
%defattr(644,root,root,755)
%attr(770,root,cvs) %dir %{_cvs_root}
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rc-inetd/cvs
