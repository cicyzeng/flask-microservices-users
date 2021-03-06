"""empty message

Revision ID: 606d8f1e2e55
Revises: 
Create Date: 2017-10-26 22:11:13.688863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '606d8f1e2e55'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['email'])
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###
