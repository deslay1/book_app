#ifndef Py_STRCMP_H
#define Py_STRCMP_H

#ifdef __cplusplus
extern "C" {
#endif

PyAPI_FUNC(int) PSellerOrBuyerS_mystrnicmp(const char *, const char *, Py_ssize_t);
PyAPI_FUNC(int) PSellerOrBuyerS_mystricmp(const char *, const char *);

#ifdef MS_WINDOWS
#define PSellerOrBuyerS_strnicmp strnicmp
#define PSellerOrBuyerS_stricmp stricmp
#else
#define PSellerOrBuyerS_strnicmp PSellerOrBuyerS_mystrnicmp
#define PSellerOrBuyerS_stricmp PSellerOrBuyerS_mystricmp
#endif

#ifdef __cplusplus
}
#endif

#endif /* !Py_STRCMP_H */
