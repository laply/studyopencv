template<typename _Tp> class Point_
{
public:
    Point_();
    Point_(_Tp _x, _Tp _y);
    Point_(const Point__& pt);

    Point_& operator = (const Point_& pt);

    _Tp dot(const Point_& pt) const;

    double ddot(const Point_& pt) const;
    double cross(const Point_& pt) const;
    double inside(const Rect_<_Tp>& r) const;
    ...


    _Tp x, y;
};

