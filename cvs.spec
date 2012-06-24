Summary:	Concurrent Versioning System
Summary(de):	Concurrent-Versioning-System
Summary(fr):	CVS : Concurrent Versioning System
Summary(pl):	Concurrent Versioning System
Summary(tr):	S�r�m denetim sistemi
Name:		cvs
Version:	1.10.5
Release:     	3
Copyright:	GPL
Group:		Development/Version Control
Group(pl):	Programowanie/Zarzadzanie wersjami
Source0:	http://download.cyclic.com/pub/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:		cvs-tmprace.patch
Patch1:		cvs-info.patch
URL:		http://www.cyclic.com/
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root

%description
CVS is a front end to the rcs(1) revision control system which extends the
notion of revision control from a collection of files in a single directory
to a hierarchical collection of directories consisting of revision
controlled files. These directories and files can be combined together to
form a software release. CVS provides the functions necessary to manage
these software releases and to control the concurrent editing of source
files among multiple software developers.

%description -l de
CVS ist ein Frontend f�r das RCS(1)-Revisionskontrollsystem, das den Begriff
der Revisionskontrolle von einer Sammlung von Dateien in einem einzelnen
Verzeichnis auf eine ganze Hierarchie ausweitet, bestehend aus
revisionskontrollierten Dateien. Diese Verzeichnisse und Dateien lassen sich
zu einer Software-Release kombinieren. CVS bietet die Funktionen, die zur
Verwaltung von Software-Releases und zur �berwachung der gleichzeitigen
Bearbeitung von Quelldateien durch mehrere Software- Entwickler notwendig
sind.

%description -l fr
CVS est un frontal pour le syst�me de contr�le de r�vision rcs(1) qui �tend
la notion de contr�le de r�vision d'un ensemble de fichiers plac�s dans un
seul r�pertoire � un ensemble hi�rarchis� de r�pertoires contenant des
fichiers contr�l�s. Ces r�pertoires et fichiers peuvent �tre combin�s pour
former une version de logiciel. CVS offre les fonctions n�cessaires pour
g�rer ces versions et pour contr�ler la modification simultan�e des fichiers
sources entre les diff�rents d�eloppeurs.

%description -l pl
CVS jest nak�adk� na rcs (Revision Control System, czyli w wolnym
t�umaczeniu system kontroli wersji zasob�w), kt�ry rozszerza mo�liwo�ci
rcs'a z narz�dzia do kontroli zbioru plik�w w pojedynczym katalogu o
mo�liwo�� kontroli zbioru hierarhicznie u�o�onych katalog�w z plikami. Z
pomoc� CVS w �atwy spos�b mo�na zarz�dza� kodem �r�d�owym opracowywanym przez
nawet bardzo du�e zesp�y programist�w umo�liwiaj�c �ledzenie i kontrol�
wszystkich zmian w trakcie pracy nad projektami i wypuszczaniem pe�nych
wersji oprogramowania (release).

%description -l tr
CVS (Concurrent Versioning System), tek bir dizindeki dosya toplulu�unun
s�r�m denetimini, denetimi yap�lm�� dizinlerin hiyerar�ik toplulu�una
geni�leten rcs(1) s�r�m denetim sisteminin �n y�z�d�r. Bu dizin ve dosyalar,
bir yaz�l�m yay�n� olu�turma amac�yla biraraya getirilebilir. CVS, bu
yaz�l�m yay�nlar�n�n y�netilmesini ve kaynak dosyalar� bak�m�n�n birden �ok
yaz�l�m geli�tiricisi taraf�ndan e�zamanl� olarak yap�lmas�n� kontrol etmek
i�in gereken i�levleri sa�lar.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--enable-server \
	--enable-client
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr
make install-info prefix=$RPM_BUILD_ROOT/usr

strip $RPM_BUILD_ROOT/usr/bin/cvs

gzip -9nf $RPM_BUILD_ROOT/usr/{info/cvs*,man/man{1,5,8}/*} doc/*.ps \
	BUGS FAQ MINOR-BUGS NEWS PROJECTS TODO README ChangeLog

%post
/sbin/install-info /usr/info/cvs.info.gz /etc/info-dir
/sbin/install-info /usr/info/cvsclient.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete /usr/info/cvs.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/cvsclient.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,FAQ,MINOR-BUGS,NEWS,PROJECTS,TODO,README,ChangeLog}.gz
%doc doc/*.ps.gz

%attr(755,root,root) /usr/bin/*
%attr(  -, root, root) /usr/lib/cvs

/usr/man/man[158]/*
/usr/info/cvs*

%changelog
* Mon Apr 19 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.10.5-3]
- recompiles on new rpm.

* Tue Mar  9 1999 Micha� Kuratczyk <kura@pld.org.pl>
  [1.10.5-2]
- gzipping documentation (instead bzipping)

* Mon Feb 22 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.10.5-1]
- removed man group from man pages.

* Wed Jan 26 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.10.4-1d]
- added compressing %doc,
- added cvs-info.patch,
- added Group(pl).

* Wed Dec 23 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.10.3-3]
- standarized {un}registering info pages,
- cvs info pages moved to section "Version Control:",
- added gzipping man pages.

* Sun Sep  6 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.10.1-2]
- fix race conditions in cvsbug/rcs2log.

* Thu Sep  3 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.10.1-1]
- removed "Requires: rcs",
- added fixed rcs2log.sh script.

* Sat Aug  1 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.9.29-1]
- added pl translation,
- added -q %setup parametr,
- added URL,
- Changed Source url,
- spec file rewritten for using Buildroot,
- added ChangeLog to %doc,
- added %clean section,
- added %defattr and %attr macros in %files (allows building package from
  non-root account).

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added install-info stuff
- added changelog section
